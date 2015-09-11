'''
Created on Sep 11, 2015

@author: ggomarr
'''

import subprocess

class alarm:
    '''
    Create the Julius process and offer methods to read lines from it, or read text from the console
    '''
    
    def __init__(self, listener_type='shell', julius_conf=''):
        self.conf=julius_conf
        if listener_type=='mic':
            self.launch_alarm=self.launch_alarm_mic
            self.listen_for_alarm=self.listen_for_alarm_mic
        else:
            self.launch_alarm=self.launch_alarm_shell
            self.listen_for_alarm=self.listen_for_alarm_shell

    def launch_alarm_mic(self):
        self.proc = subprocess.Popen(['julius', '-quiet', '-input', 'mic', '-C', self.conf], 
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def listen_for_alarm_mic(self):
        startstring = 'sentence1: <s> '
        endstring = ' </s>'
        phrase = ''
    
        while phrase == '':
            line = self.proc.stdout.readline().lower()
    
            if line.startswith(startstring) and line.strip().endswith(endstring):
                phrase = line.strip()[len(startstring):-len(endstring)]
                self.proc.kill()
                return phrase

    def launch_alarm_shell(self):
        return True
        
    def listen_for_alarm_shell(self):
        phrase = raw_input('?> ').lower()
        return phrase
        
if __name__ == "__main__":        
    julius_conf = '/home/ggomarr/eclipse/workspace/PyAIML/src/alarm/julius/julian.jconf'
    end_cue  = 'computer shut down'
    last_phrase = ''
    
    alm = alarm('mic', julius_conf)
    while last_phrase != end_cue:
        alm.launch_alarm()
        last_phrase = alm.listen_for_alarm()
        print last_phrase