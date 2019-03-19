#########################################
####nCore CouchPotato TorrentProvider####
############# @by gala ##################
############### 2015 ####################
#########################################
from couchpotato.core.logger import CPLog
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
import json

log = CPLog(__name__)

class nCore(TorrentProvider, MovieProvider):
    urls = {
        'login': 'https://ncore.cc/login.php',
        'search': 'https://ncore.cc/torrents.php?oldal=%s&kivalasztott_tipus=%s&mire=%s&miben=name&tipus=kivalasztottak_kozott&submit.x=0&submit.y=0&submit=Ok&tags=&searchedfrompotato=true&jsons=true'
    }

    http_time_between_calls = 1  # seconds

    def _searchOnTitle(self, title, movie, quality, results):
        hu_extra_score = 500 if self.conf('prefer_hu') else 0
        en_extra_score = 500 if self.conf('prefer_en') else 0

        self.doSearch(title, self.conf('hu_categories'), hu_extra_score, results)
        self.doSearch(title, self.conf('en_categories'), en_extra_score, results)

    def doSearch(self, title, categories, extra_score, results):
        url = self.urls['search'] % (1, categories, tryUrlencode(title))
        try:
            data = self.getJsonData(url, data='some random stuff just to ignore cache')
            log.info('Number of torrents found on nCore = ' + data['total_results'])

            total_result_count = int(data['total_results'])
            item_per_page_count = int(data['perpage'])

            page_count = total_result_count / item_per_page_count
            left_over = total_result_count % item_per_page_count
            if left_over > 0:
                page_count += 1

            ncore_results = data['results']
            page_index = 2
            while page_index <= page_count:
                url = self.urls['search'] % (page_index, categories, tryUrlencode(title))
                data = self.getJsonData(url, data='some random stuff just to ignore cache')
                ncore_results.extend(data['results'])
                page_index += 1

            for d in ncore_results:
                to_append = {
                    'id': d['torrent_id'],
                    'leechers': d['leechers'],
                    'seeders': d['seeders'],
                    'name': d['release_name'],
                    'url': d['download_url'],
                    'detail_url': d['details_url'],
                    'size': tryInt(d['size']) / (1024 * 1024),
                    'score': extra_score
                }

                imdb_id = d.get('imdb_id')
                if imdb_id and isinstance(imdb_id, unicode):
                    to_append.update({'description': imdb_id})

                results.append(to_append)
        except:
            log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))

    def getLoginParams(self):
        return {
            'nev': str(self.conf('username')),
            'pass': str(self.conf('password')),
            'submitted': 1
        }

    def successLogin(self, output):
       return 'exit.php' in output.lower()

    loginCheckSuccess = successLogin
