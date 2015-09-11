'''
Created on Sep 11, 2015

@author: ggomarr
'''

from speaker.speaker import speaker
from listener.listener import listener
from alarm.alarm import alarm
from brain.brain import brain

import parameters

if __name__ == "__main__":    
    alm = alarm(parameters.listener_type, parameters.julius_conf)
    lsn = listener(parameters.listener_type,parameters.min_energy_threshold)
    brn = brain(parameters.bot_brain)
    spk = speaker(parameters.speaker_type, parameters.speaker_lang)
        
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
            last_answer = brn.process_phrase(last_input)
            spk.say(last_answer)

    spk.say(parameters.goodbye)
    