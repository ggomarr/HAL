'''
Created on Sep 11, 2015

@author: ggomarr
'''

import gtts, pyttsx
import requests, tempfile, os

class speaker:
    '''
    Use either the Google Text To Speech engine, the espeak engine, or the shell to speak
    '''

    def __init__(self, speaker_type='pyttsx', speaker_lang='en'):
        if speaker_type == 'gTTS':
            self.say = self.say_gTTS
            self.lang=speaker_lang
        elif speaker_type == 'pyttsx':
            self.say = self.say_pyttsx
        else:
            self.say = self.say_shell
    
    def say_gTTS(self, txt):
        if txt=='':
            txt='Sorry, I didn\'t get that. I do not know what to say!'
        temp_mp3 = tempfile.mkstemp()[1]
        try:
            speech = gtts.gTTS(text=txt,lang=self.lang)
            speech.save(temp_mp3)
            os.system("mpg123 " + temp_mp3)
        except requests.exceptions.ConnectionError:
            print "Error: No connection or connection timed out. Reverting to pyttsx."
            self.say = self.say_pyttsx
            self.say(txt)
        os.remove(temp_mp3)
        
    def say_pyttsx(self, txt):
        if txt=='':
            txt='Sorry, I didn\'t get that. I do not know what to say!'
        speech = pyttsx.init()
        speech.say(txt)
        speech.runAndWait()
        del speech
        
    def say_shell(self, txt):
        if txt=='':
            txt='Sorry, I didn\'t get that. I do not know what to say!'
        print 'Bot >>> ' + txt

if __name__ == "__main__":
    spk = speaker('gTTS')
    spk.say('Daisy, Daisy, give me your answer, do, I\'m half crazy all for the love of you. It won\'t be a stylish marriage, I can\'t afford a carriage, But you\'d look sweet upon the seat Of a bicycle made for two.')
