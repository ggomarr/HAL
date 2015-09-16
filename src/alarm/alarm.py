'''
Created on Sep 11, 2015

@author: ggomarr
'''

import subprocess
import pyaudio, pocketsphinx
import parameters.alarm_conf as parameters

class alarm:
    '''
    Create the Julius process or the Sphinx decoder and methods to read from them, or read text from the console
    '''
    
    def __init__(self, alarm_type=parameters.alarm_type):
        if alarm_type==parameters.type_julius:
            self.launch_alarm=self.launch_alarm_julius
            self.listen_for_alarm=self.listen_for_alarm_julius
        elif alarm_type==parameters.type_sphinx:
            self.launch_alarm=self.launch_alarm_sphinx
            self.listen_for_alarm=self.listen_for_alarm_sphinx
            cfg = pocketsphinx.Decoder.default_config()
            cfg.set_string('-hmm', parameters.sphinx_acoustic_model)
            cfg.set_string('-lm', parameters.sphinx_lang + '.lm')
            cfg.set_string('-dict', parameters.sphinx_lang + '.dic')
            cfg.set_string('-kws', parameters.sphinx_lang + '.keyphrases')
            cfg.set_string('-logfn', '/dev/null')
            self.sphinx = pocketsphinx.Decoder(cfg)
            audio_source = pyaudio.PyAudio()
            self.audio_stream = audio_source.open(format=pyaudio.paInt16, channels=1, rate=16000,
                                             input=True, frames_per_buffer=1024)
        else:
            self.launch_alarm=self.launch_alarm_shell
            self.listen_for_alarm=self.listen_for_alarm_shell

    def launch_alarm_julius(self):
        self.proc = subprocess.Popen(['julius', '-quiet', '-input', 'mic', '-C', parameters.julius_conf], 
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def listen_for_alarm_julius(self):
        phrase = ''
    
        while phrase == '':
            line = self.proc.stdout.readline().lower()
    
            if line.startswith(parameters.startstring) and line.strip().endswith(parameters.endstring):
                phrase = line.strip()[len(parameters.startstring):-len(parameters.endstring)]
                self.proc.kill()
                return phrase

    def launch_alarm_sphinx(self):
        return True

    def listen_for_alarm_sphinx(self):
        self.audio_stream.start_stream()
        in_speech_bf = True
        self.sphinx.start_utt()
        while True:
            buf = self.audio_stream.read(1024)
            if buf:
                self.sphinx.process_raw(buf, False, False)
#                try:
#                    if  self.sphinx.hyp().hypstr != '':
#                        print 'Partial decoding result:', self.sphinx.hyp().hypstr
#                except AttributeError:
#                    pass
                if self.sphinx.get_in_speech() != in_speech_bf:
                    in_speech_bf = self.sphinx.get_in_speech()
                    if not in_speech_bf:
                        self.sphinx.end_utt()
                        try:
                            if  self.sphinx.hyp().hypstr != '':
                                self.audio_stream.stop_stream()
                                return self.sphinx.hyp().hypstr.lower()
                        except AttributeError:
                            pass
                        self.sphinx.start_utt()
            else:
                break
        self.sphinx.end_utt()
        print 'An Error occured:', self.sphinx.hyp().hypstr

    def launch_alarm_shell(self):
        return True
        
    def listen_for_alarm_shell(self):
        phrase = raw_input('YOU >>> ').lower()
        return phrase
        
if __name__ == "__main__":        
    end_cue  = 'computer wake up'
    last_phrase = ''
    
    alm = alarm(parameters.alarm_type)
    while last_phrase != end_cue:
        alm.launch_alarm()
        last_phrase = alm.listen_for_alarm()
        print last_phrase