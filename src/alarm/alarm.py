'''
Created on Sep 11, 2015

@author: ggomarr
'''

import subprocess
import parameters.alarm_conf as parameters

class alarm:
    '''
    Create the Julius process and offer methods to read lines from it, or read text from the console
    '''
    
    def __init__(self, alarm_type=parameters.alarm_type):
        if alarm_type==parameters.type_julius:
            self.launch_alarm=self.launch_alarm_mic
            self.listen_for_alarm=self.listen_for_alarm_mic
        else:
            self.launch_alarm=self.launch_alarm_shell
            self.listen_for_alarm=self.listen_for_alarm_shell

    def launch_alarm_mic(self):
        self.proc = subprocess.Popen(['julius', '-quiet', '-input', 'mic', '-C', parameters.julius_conf], 
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def listen_for_alarm_mic(self):
        phrase = ''
    
        while phrase == '':
            line = self.proc.stdout.readline().lower()
    
            if line.startswith(parameters.startstring) and line.strip().endswith(parameters.endstring):
                phrase = line.strip()[len(parameters.startstring):-len(parameters.endstring)]
                self.proc.kill()
                return phrase

    def launch_alarm_shell(self):
        return True
        
    def listen_for_alarm_shell(self):
        phrase = raw_input('YOU >>> ').lower()
        return phrase
        
if __name__ == "__main__":        
    end_cue  = 'computer shut down'
    last_phrase = ''
    
    alm = alarm(parameters.alarm_type)
    while last_phrase != end_cue:
        alm.launch_alarm()
        last_phrase = alm.listen_for_alarm()
        print last_phrase