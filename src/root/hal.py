'''
Created on Sep 11, 2015

@author: ggomarr
'''

from speaker.speaker import speaker
from listener.listener import listener
from alarm.alarm import alarm
from brain.brain import brain

import parameters.cues_conf as parameters

if __name__ == "__main__":    
    alm = alarm()
    lsn = listener()
    brn = brain()
    spk = speaker()
        
    spk.say(parameters.greeting)
    
    last_input = ''
    while last_input != parameters.end_cue:
        alm.launch_alarm()
        last_phrase = alm.listen_for_alarm()
        if last_phrase == parameters.end_cue:
            break
        spk.say(parameters.serve)
        while True:
            last_input = lsn.listen_for_input()
            if last_input == parameters.end_cue:
                break
            last_answer = brn.parse_input(last_input)
            spk.say(last_answer)

    spk.say(parameters.goodbye)
    