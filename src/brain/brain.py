'''
Created on Sep 11, 2015

@author: ggomarr
'''

from speaker.speaker import speaker
from listener.listener import listener
from chatbot.chatbot import chatbot
from plexcontroller.plexcontroller import plexcontroller
import parameters.brain_conf as parameters
import parameters.cues_conf as cues
import parameters.regex_conf as regex
import re, random

class brain:
    '''
    Create the central processing system and offer methods to read answers from it
    '''
    
    def __init__(self):
        self.bot = chatbot()
        self.spk = speaker()
        self.lsn = listener()
        self.plx = plexcontroller()

    def take_over(self):
        self.spk.say(cues.serve)
        active = True
        while active:
            phrase = self.lsn.listen_for_input()
            parsed = self.parse_input(phrase, regex.reg_main)
            if   parsed[0] == parameters.plex_action:
                if parsed[1] == parameters.pause_action:
                    self.plx.pause_show()
                    self.spk.say(cues.success)
                elif parsed[1] == parameters.resume_action:
                    self.plx.resume_show()
                    self.spk.say(cues.success)
                elif parsed[1] == parameters.stop_action:
                    self.plx.stop_show()
                    self.spk.say(cues.success)
                else: # There is only play left
                    showtype_parsed = self.parse_input(phrase, regex.reg_showtype)
                    unwatched_parsed = self.parse_input(phrase, regex.reg_unwatched)
                    show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                    if len(show_list) == 1:
                        show_to_play = show_list[0][1]
                    elif showtype_parsed[0] == parameters.unknown:
                        self.spk.say(cues.showtype)
                        showtype_phrase = self.lsn.listen_for_input()
                        showtype_parsed = self.parse_input(showtype_phrase, regex.reg_showtype)
                    show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                    if len(show_list) == 1:
                        show_to_play = show_list[0][1]
                    elif unwatched_parsed[0] == parameters.unknown:
                        self.spk.say(cues.unwatched)
                        unwatched_phrase = self.lsn.listen_for_input()
                        unwatched_parsed = self.parse_input(unwatched_phrase, regex.reg_yesno)
                    show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                    if len(show_list) == 1:
                        show_to_play = show_list[0][1]
                    else:
                        selected_option = self.propose_options(show_list)
                        show_to_play = show_list[selected_option][1]
                    if self.plx.play_show(show_to_play):
                        self.spk.say(cues.success)
                    else:
                        self.spk.say(cues.no_client)
            elif parsed[0] == parameters.wiki_action:
                self.spk.say([ 'There should be a wiki action here, on ' + parsed[1] ])
            elif parsed[0] == parameters.chatbot_action:
                answer = self.bot.process_phrase(parsed[1])
                self.spk.say([ answer ])
            elif parsed[0] == parameters.police_action:
                self.spk.say(cues.police)
            elif parsed[0] == parameters.noidea_action:
                self.spk.say(cues.repeat)
            else: # same as elif parsed[0] == parameters.sleep_action:
                self.spk.say(cues.sleep)
                active = False

    def parse_input(self, phrase, regex_context=regex.reg_main):
        if phrase == '':
            answer = [ parameters.noidea_action, phrase ]
        else:
            answer = [ parameters.chatbot_action, phrase ]
            for reg in regex_context:
                parser = re.compile(reg[0])
                finder = parser.search(phrase)
                if finder:
                    if reg[2] > -1:
                        answer = [ reg[1], finder.groups()[reg[2]] ]
                    else:
                        answer = [ reg[1], phrase ]
                    break
        return answer
        
    def propose_options(self, options):
        i = 1
        for option in options:
            self.spk.say([ str(i) + '. ' + option[0] ])
            selection = self.lsn.listen_for_input(parameters.option_delay)
            if selection <> '':
                if selection.isdigit():
                    selection = int(selection)
                else:
                    selection = i
                break
            i = i + 1
        if selection == '':
            selection = self.lsn.listen_for_input()
            if selection.isdigit():
                selection = int(selection)
        if selection > len(options):
            self.spk.say(cues.random)
            selection = random.choice(range(1,len(options)+1))
        return selection-1
        
if __name__ == "__main__":        
    brn = brain()
    while True:
        answer = brn.parse_input(raw_input("YOU >>> "))
        print answer
    