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
        'search': 'https://ncore.cc/torrents.php?kivalasztott_tipus=%s&mire=%s&miben=name&tipus=kivalasztottak_kozott&submit.x=0&submit.y=0&submit=Ok&tags=&searchedfrompotato=true&jsons=true'
    }

    http_time_between_calls = 1  # seconds

    def _searchOnTitle(self, title, movie, quality, results):
        hu_extra_score = 500 if self.conf('prefer_hu') else 0
        en_extra_score = 500 if self.conf('prefer_en') else 0

        self.doSearch(title, self.conf('hu_categories'), hu_extra_score, results)
        self.doSearch(title, self.conf('en_categories'), en_extra_score, results)

    def doSearch(self, title, categories, extra_score, results):
        url = self.urls['search'] % (categories, tryUrlencode(title))
        try:
            data = self.getJsonData(url)
            log.info('Number of torrents found on nCore = ' + str(data['total_results']))
            for d in data['results']:
                results.append({
                    'id': d['torrent_id'],
                    'leechers': d['leechers'],
                    'seeders': d['seeders'],
                    'name': d['release_name'],
                    'url': d['download_url'],
                    'detail_url': d['details_url'],
                    'size': tryInt(d['size']) / (1024 * 1024),
                    'score': extra_score,
                })
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
