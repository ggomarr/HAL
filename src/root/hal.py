'''
Created on Sep 11, 2015

@author: ggomarr
'''

from alarm.alarm import alarm
from brain.brain import brain

import parameters.cues_conf as cues

if __name__ == "__main__":    
    alm = alarm()
    brn = brain()

    brn.spk.say(cues.greeting)
            
    while True:
        phrase = ''
        while phrase not in cues.activate:
            alm.launch_alarm()
            phrase = alm.listen_for_alarm()
        if phrase in cues.end_cue:
            break
        brn.take_over()

    brn.spk.say(cues.goodbye)
    