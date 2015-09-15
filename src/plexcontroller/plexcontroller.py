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
        if unwatched_only:
            result = [ show for show in result if show.viewCount == 0 ]
        answer =          [ [ 'the ' + show.type + ' ' + show.title, show.key[18:] ]
                            for show in result if show.type == 'movie' ]
        answer = answer + [ [ 'the ' + show.type + ' ' + show.title, show.key[18:] ]
                            for show in result if show.type == 'show' ]
        answer = answer + [ [ 'the ' + show.type + ' ' + show.title + ' from the show ' + show.show().title, show.key[18:] ]
                            for show in result if show.type == 'episode' ]
        return answer
        
    def play_show(self, show_key, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except NotFound:
            return False
        show = self.plex.library.getByKey(show_key)
        client.playMedia(show)
        return True

    def pause_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except NotFound:
            return False
        client.select()
        client.select()
        return True

    def resume_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.server.NotFound:
            return False
        client.select()
        client.select()
        return True

    def stop_show(self, on_client=parameters.default_client):
        try:
            client = self.plex.client(on_client)
        except plexapi.server.NotFound:
            return False
        client.back()
        return True

if __name__ == "__main__":
    print "Hello world!"