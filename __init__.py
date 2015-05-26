#########################################
####nCore CouchPotato TorrentProvider####
############# @by gala ##################
############### 2015 ####################
#########################################
from .main import nCore


def autoload():
    return nCore()


config = [{
              'name': 'ncore',
              'groups': [
                  {
                      'tab': 'searcher',
                      'list': 'torrent_providers',
                      'name': 'nCore',
                      'description': 'See <a href="https://ncore.cc/">nCore</a>',
                      'wizard': True,
                      'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABqUlEQVQ4jY3SPWsUYRTF8d86k7gbNb4loKxiEFKk0UJIo4KQQkgtduYLmEIrDVhZ2buxsLKyzQfwGwT7jY1IdEVxJbjG7OtkLfZOMiYWGXgYeObc/zn3zi0tUsEL3McFR3u+4g2eJ7O83OThFidLSEMxRIYB+uhiBz/Q4FSb26dJS4u0P1K+gmlMBGA3AFkB1MNvNONco5lmlM8jP+UD7oNCirG4P4HWyGcqFa4V/MFn/PwPIMG5KE4KreZvWUzmyeqq6/Pzh6fWaHi6suJTva4cLe4BsojYjw/brZbXtZovjcYo8uSkB0tLarWamwsLLkaqPUA+oG70/2Fjw7u1NVMBbWG6WvV4eVkndP0ioB+AXiQYhmgsRN1C5NzsUIJuQZgD2vZ3ICvMqpigdJfhd5wN8sTcnAy/6nWVEO4gq1Zdqla9X183Hne3csAmzuA4OuGSRHG+A+1wFpoO7iAdGv3/JBKINtqF4oH9jewV7iBN6W0zPsQ4Sv5d4ewAIF+sY6P6ZjLL5QE3tiJWtxAxH2zumjsnuDpq+1WKRzPsznAPU472fMNbPPsLszaznIb1BQAAAAAASUVORK5CYII=',
                      'options': [
                          {
                              'name': 'enabled',
                              'type': 'enabler',
                              'default': False,
                          },
                          {
                              'name': 'username',
                              'default': '',
                          },
                          {
                              'name': 'password',
                              'default': '',
                              'type': 'password',
                          },
                          {
                              'name': 'seed_ratio',
                              'label': 'Seed ratio',
                              'type': 'float',
                              'default': 1,
                              'description': 'Will not be (re)moved until this seed ratio is met.',
                          },
                          {
                              'name': 'seed_time',
                              'label': 'Seed time',
                              'type': 'int',
                              'default': 96,
                              'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                          },
                          {
                              'name': 'prefer_hu',
                              'label': 'Prefer Hungarian',
                              'type': 'bool',
                              'default': False,
                              'description': 'Favors Hungarian dubbed results.',
                          },
                          {
                              'name': 'prefer_en',
                              'label': 'Prefer English/Original',
                              'type': 'bool',
                              'default': False,
                              'description': 'Favors English or original language over Hungarian dubbed results.',
                          },
                          {
                              'name': 'hu_categories',
                              'advanced': True,
                              'default': 'xvid_hun,dvd_hun,dvd9_hun,hd_hun',
                              'description': 'Search categories for Hungarian dubbed movies',
                          },
                          {
                              'name': 'en_categories',
                              'advanced': True,
                              'default': 'xvid,dvd,dvd9,hd',
                              'description': 'Search categories for English or original language movies',
                          },
                          {
                              'name': 'extra_score',
                              'advanced': True,
                              'type': 'int',
                              'default': 0,
                              'description': 'Starting score for each release found via this provider.',
                          },
                      ],
                  },
              ],
          }]
