'''
Created on Sep 13, 2015

@author: ggomarr
'''

import plexapi.server
import parameters.plexcontroller_conf as parameters

class plexcontroller:
    '''
    Provides modules to interact with plex
    '''

    def __init__(self, plex_server=parameters.plex_server):
        self.plex = plexapi.server.PlexServer(plex_server)       
        
    def search_shows(self, search_target, show_type='', unwatched_only=False):
        result = self.plex.search(search_target, show_type)
        
        mov_lst = [ show for show in result if show.type == 'movie' ]
        sho_lst = [ show for show in result if show.type == 'show' ]
        epi_lst = [ show for show in result if show.type == 'episode' ]

        answer = []
        for mov in mov_lst:
            if not unwatched_only or mov.viewCount == 0:
                mov_key = mov.key.split('/')[3]
                answer = answer + [ [ 'The movie ' + mov.title, mov_key ] ]
        for sho in sho_lst:
            sho_key = sho.key.split('/')[3]
            if self.plex.library.getByKey(sho_key).unwatched():
                sho_epi = self.plex.library.getByKey(sho_key).unwatched()[0]
                epi_key = sho_epi.key.split('/')[3]
                answer = answer + [ [ 'The show ' + sho.title, epi_key ] ]
            elif not unwatched_only:
                sho_epi = self.plex.library.getByKey(sho_key).episodes()[0]
                epi_key = sho_epi.key.split('/')[3]
                answer = answer + [ [ 'The show ' + sho.title, epi_key ] ]
        for epi in epi_lst:
            if not unwatched_only or epi.viewCount == 0:
                epi_key = epi.key.split('/')[3]
                answer = answer + [ [ 'The episode ' + epi.title + ' from the show ' + epi.show().title, epi_key ] ]
        return answer
        
    def play_show(self, show_key, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.exceptions.NotFound:
            return False
        show = self.plex.library.getByKey(show_key)
        client.playMedia(show)
        return True

    def pause_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.exceptions.NotFound:
            return False
        client.select()
        client.select()
        return True

    def resume_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.exceptions.NotFound:
            return False
        client.select()
        client.select()
        return True

    def stop_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.exceptions.NotFound:
            return False
        client.back()
        return True

if __name__ == "__main__":
    plx = plexcontroller()
    print plx.search_shows('3gqr3gq1')