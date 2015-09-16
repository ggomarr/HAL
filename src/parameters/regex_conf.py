'''
Created on Sep 14, 2015

@author: ggomarr
'''
import parameters.brain_conf as actions

reg_main      = [ [ 'go to sleep|goodbye|all for now|you later',
                    actions.sleep_action, -1 ],
                  [ 'this is an emergency|call the police|defcon 1|^emergency|^police|^defcon',
                    actions.police_action, -1 ],
                  [ '(tell|gather|find|know|retrieve|search|look|get)(.*)?(about|on|for)? (the )?(.*)( on| in| from) wikipedia',
                    actions.wiki_action, 4 ],
                  [ '(tell|gather|find|know|retrieve|search|look|get)(.*)?(about|on|for) (the )?(.*)',
                    actions.wiki_action, 4 ], 
                  [ '(pause|resume|stop)( plex| the show| the movie| the episode)',
                    actions.plex_action, 0 ],
                  [ '(play) (.*)',
                    actions.plex_action, 1 ] ]

reg_yesno     = [ [ 'yes|sure|please|positive|affirmative|absolutely|you got it|exactly',
                    actions.positive_answer, -1 ],
                  [ '.*' ,
                    actions.negative_answer, -1 ] ]

reg_showtype  = [ [ 'movie',
                    actions.movie_type, -1 ],
                  [ 'show' ,
                    actions.show_type, -1 ],
                  [ 'episode' ,
                    actions.episode_type, -1 ],
                  [ '.*' ,
                    actions.unknown, -1 ] ]

reg_unwatched = [ [ 'unwatched|next|new|latest',
                    actions.positive_answer, -1 ],
                  [ '.*' ,
                    actions.unknown, -1 ] ]