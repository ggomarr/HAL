'''
Created on Sep 8, 2015

@author: ggomarr
'''

import aiml
import parameters.chatbot_conf as parameters

class chatbot:
    '''
    Create the natural conversation processing system and offer methods to read answers from it
    '''
    
    def __init__(self, bot_brain=parameters.bot_brain,bot_persona=parameters.bot_persona):
        self.bot_brain = bot_brain
        self.bot_persona = bot_persona
        self.bot = aiml.Kernel()
        try:
            self.bot.loadBrain(bot_brain)
        except IOError:            
            self.regenerate_brain()
        self.regenerate_persona()
            
    def process_phrase(self, phrase=''):
        answer = self.bot.respond(phrase)
        return answer
        
    def regenerate_brain(self):
        for bot_lib in parameters.bot_libs:
            self.bot.learn(parameters.bot_lib_root + bot_lib)
        self.bot.saveBrain(self.bot_brain)

    def regenerate_persona(self):
        persona_file = open(self.bot_persona)
        bot_predicates = persona_file.readlines()
        persona_file.close()
        for bot_predicate in bot_predicates:
            key_value = bot_predicate.split('::')
            if len(key_value) == 2:
                self.bot.setBotPredicate(key_value[0], key_value[1].rstrip('\n'))
        
if __name__ == "__main__":
    end_cue  = 'computer shut down'
    input_txt = ''
    
    bot = chatbot(parameters.bot_brain)
    while True:
        input_txt = raw_input("YOU >>> ")
        if input_txt == end_cue:
            break
        answer_txt = bot.process_phrase(input_txt)
        print "BOT >>> " + answer_txt