'''
Created on Sep 11, 2015

@author: ggomarr
'''

import gtts, pyttsx
import requests, tempfile, os
import parameters.speaker_conf as parameters

class speaker:
    '''
    Use either the Google Text To Speech engine, the espeak engine, or the shell to speak
    '''

    def __init__(self, speaker_type=parameters.speaker_type):
        if speaker_type == parameters.type_gTTS:
            self.say = self.say_gTTS
        elif speaker_type == parameters.type_pyttsx:
            self.say = self.say_pyttsx
        else:
            self.say = self.say_shell
    
    def say_gTTS(self, txt):
        if txt=='':
            txt='Sorry, I do not know what to say!'
        temp_mp3 = tempfile.mkstemp()[1]
        try:
            speech = gtts.gTTS(text=txt,lang=parameters.speaker_lang)
            speech.save(temp_mp3)
            os.system("mpg123 " + temp_mp3)
        except requests.exceptions.ConnectionError:
            print "Error: No connection or connection timed out. Reverting to pyttsx."
            self.say = self.say_pyttsx
            self.say(txt)
        os.remove(temp_mp3)
        
    def say_pyttsx(self, txt):
        if txt=='':
            txt='Sorry, I do not know what to say!'
        speech = pyttsx.init()
        speech.say(txt)
        speech.runAndWait()
        del speech
        
    def say_shell(self, txt):
        if txt=='':
            txt='Sorry, I do not know what to say!'
        print 'Bot >>> ' + txt

if __name__ == "__main__":
    spk = speaker('shell')
    spk.say('Daisy, Daisy, give me your answer, do, I\'m half crazy all for the love of you. It won\'t be a stylish marriage, I can\'t afford a carriage, But you\'d look sweet upon the seat Of a bicycle made for two.')
