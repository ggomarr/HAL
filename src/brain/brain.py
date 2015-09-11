'''
Created on Sep 11, 2015

@author: ggomarr
'''

import aiml

class brain:
    '''
    Create the central processing system and offer methods to read answers from it
    '''
    
    def __init__(self, bot_brain):
        self.bot_brain = bot_brain
        self.bot = aiml.Kernel()
        self.bot.loadBrain(bot_brain)

    def process_phrase(self, phrase=''):
        answer = self.bot.respond(phrase)
        return answer
        
if __name__ == "__main__":        
    bot_brain = '/home/ggomarr/eclipse/workspace/PyAIML/01 Alice/brain/alice.brain'
    end_cue  = 'computer shut down'
    input_txt = ''
    
    brn = brain(bot_brain)
    while input_txt != end_cue:
        input_txt = raw_input("?> ")
        answer_txt = brn.process_phrase(input_txt)
        print answer_txt