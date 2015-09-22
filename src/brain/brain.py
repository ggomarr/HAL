'''
Created on Sep 11, 2015

@author: ggomarr
'''

from speaker.speaker import speaker
from listener.listener import listener
from chatbot.chatbot import chatbot
from plexcontroller.plexcontroller import plexcontroller
from wikireader.wikireader import wikireader
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
        self.wkp = wikireader()

    def take_over(self):
        self.spk.say(cues.serve)
        active = True
        while active:
            phrase = self.lsn.listen_for_input()
            parsed = self.parse_input(phrase, regex.reg_main)
            if   parsed[0] == parameters.plex_action:
                if parsed[1] == parameters.pause_action:
                    if   self.plx.pause_show():
                        self.spk.say(cues.success)
                    else:
                        self.spk.say(cues.no_client)
                elif parsed[1] == parameters.resume_action:
                    if self.plx.resume_show():
                        self.spk.say(cues.success)
                    else:
                        self.spk.say(cues.no_client)
                elif parsed[1] == parameters.stop_action:
                    if self.plx.stop_show():
                        self.spk.say(cues.success)
                    else:
                        self.spk.say(cues.no_client)
                else: # There is only play left
                    still_searching = True
                    selected_option = 0
                    showtype_parsed = self.parse_input(phrase, regex.reg_showtype)
                    unwatched_parsed = self.parse_input(phrase, regex.reg_unwatched)
                    show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                    if still_searching:
                        if len(show_list) < 2:
                            still_searching = False
                    if still_searching and showtype_parsed[0] == parameters.unknown:
                        self.spk.say(cues.showtype)
                        showtype_phrase = self.lsn.listen_for_input()
                        showtype_parsed = self.parse_input(showtype_phrase, regex.reg_showtype)
                        show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                        if len(show_list) < 2:
                            still_searching = False
                    if still_searching and unwatched_parsed[0] == parameters.unknown:
                        self.spk.say(cues.unwatched)
                        unwatched_phrase = self.lsn.listen_for_input()
                        unwatched_parsed = self.parse_input(unwatched_phrase, regex.reg_yesno)
                        show_list = self.plx.search_shows(parsed[1],showtype_parsed[0],unwatched_parsed[0])           
                        if len(show_list) < 2:
                            still_searching = False
                    if still_searching:
                        self.spk.say(cues.options)
                        selected_option = self.propose_options(show_list)
                        still_searching = False
                    if len(show_list) == 0:
                        self.spk.say(cues.no_show)
                    else:
                        self.spk.say(cues.playing)
                        self.spk.say([ show_list[selected_option][0] ])
                        if self.plx.play_show(show_list[selected_option][1]):
                            self.spk.say(cues.success)
                        else:
                            self.spk.say(cues.no_client)
            elif parsed[0] == parameters.wiki_action:
                if not self.wkp.retrieve_article(parsed[1]):
                    self.spk.say(cues.options)
                    selected_option = self.propose_options(self.wkp.content)
                    self.wkp.retrieve_article(self.wkp.content[selected_option][0])
                if len(self.wkp.content) == 0:
                    self.spk.say(cues.no_wiki)
                else:
                    self.spk.say(cues.wait_wiki)
                    self.spk.say( [ self.wkp.title ] )
                    self.spk.say(self.wkp.content[0])
                    for parag in self.wkp.content[1:]:
                        self.spk.say(cues.long_text)
                        continue_phrase = self.lsn.listen_for_input()
                        continue_parsed = self.parse_input(continue_phrase, regex.reg_yesno)
                        if continue_parsed[0] == parameters.negative_answer:
                            break
                        self.spk.say(parag)
                    self.spk.say(cues.success)
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
    