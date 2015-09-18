'''
Created on Sep 11, 2015

@author: ggomarr
'''

import speech_recognition
import parameters.listener_conf as parameters

class listener:
    '''
    Use either the Google Speech To Text engine or the shell to capture input
    '''

    def __init__(self, listener_type=parameters.listener_type):
        if listener_type == parameters.type_gSTT:
            self.listen_for_input = self.listen_for_input_gSTT
            self.listenah = speech_recognition.Recognizer()
            self.mic = speech_recognition.Microphone()
            print "A moment of silence, please..."
            with self.mic as source:
                self.listenah.adjust_for_ambient_noise(source)
                pass
            self.listenah.energy_threshold=max(self.listenah.energy_threshold,parameters.min_energy_threshold)
            print "Set minimum energy threshold to {}".format(self.listenah.energy_threshold)
        else:
            self.listen_for_input = self.listen_for_input_shell
    
    def listen_for_input_gSTT(self,timeout=None):
        utterance = ''
        phrase = ''
        with self.mic as source:
            try:
                utterance = self.listenah.listen(source,timeout)
            except speech_recognition.WaitTimeoutError:
                pass
            pass
        if utterance!='':
            try:
                phrase = self.listenah.recognize_google(utterance).lower()
                print 'YOU >>> ' + phrase
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                pass
        return phrase
        
    def listen_for_input_shell(self,timeout=None):
        phrase = raw_input('YOU >>> ').lower()
        return phrase

if __name__ == "__main__":
    lsn = listener(parameters.listener_type)
    print lsn.listen_for_input()