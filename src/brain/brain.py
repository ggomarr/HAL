'''
Created on Sep 11, 2015

@author: ggomarr
'''

from chatbot.chatbot import chatbot
import parameters.brain_conf as parameters

class brain:
    '''
    Create the central processing system and offer methods to read answers from it
    '''
    
    def __init__(self):
        self.chatbot = chatbot()

    def parse_input(self, phrase=''):
        answer = self.chatbot.process_phrase(phrase)
        return answer
        
if __name__ == "__main__":        
    end_cue  = 'computer shut down'
    input_txt = ''
    
    brn = brain()
    while True:
        input_txt = raw_input("YOU >>> ")
        if input_txt == end_cue:
            break
        answer_txt = brn.parse_input(input_txt)
        print answer_txt