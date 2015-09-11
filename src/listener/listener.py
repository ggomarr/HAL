'''
Created on Sep 11, 2015

@author: ggomarr
'''

import speech_recognition

class listener:
    '''
    Use either the Google Speech To Text engine or the shell to capture input
    '''

    def __init__(self, listener_type='mic',min_energy_threshold=5000):
        if listener_type == 'mic':
            self.listenah = speech_recognition.Recognizer()
            self.mic = speech_recognition.Microphone()
            self.listen_for_input = self.listen_for_input_mic
            print "A moment of silence, please..."
            with self.mic as source:
                self.listenah.adjust_for_ambient_noise(source)
                pass
            self.listenah.energy_threshold=max(self.listenah.energy_threshold,min_energy_threshold)
            print "Set minimum energy threshold to {}".format(self.listenah.energy_threshold)
        else:
            self.listen_for_input = self.listen_for_input_shell
    
    def listen_for_input_mic(self):
        print '[Waiting for you to speak]'
        with self.mic as source:
            utterance = self.listenah.listen(source)
            pass
        phrase = self.listenah.recognize_google(utterance)
        return phrase
        
    def listen_for_input_shell(self):
        phrase = raw_input('?> ').lower()
        return phrase

if __name__ == "__main__":
    lsn = listener('shell', 5000)
    print lsn.listen()