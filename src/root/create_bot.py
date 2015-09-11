'''
Created on Sep 8, 2015

@author: ggomarr
'''

# Parameters

alice_lib_root = '/home/ggomarr/eclipse/workspace/PyAIML/01 Alice/'

alice_brain = 'brain/alice.brain'

alice_libs = [ 'reduction?.safe.aiml',
               'reductions.update.aiml',
               'mp?.aiml',
               '*.aiml' ]

greeting = 'Hello! My name is Hal. Happy to serve!'
end_cue = 'goodbye'

listen = True
speak  = True

min_energy_threshold = 5000

# End parameters

import aiml
import os.path
import speech_recognition
import pyttsx

alice = aiml.Kernel()

if os.path.isfile(alice_lib_root + alice_brain):
    alice.loadBrain(alice_lib_root + alice_brain)
else:
    for alice_lib in alice_libs:
        alice.learn(alice_lib_root + alice_lib)

if listen:
    listenah = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()

    print("A moment of silence, please...")
    with mic as source:
        listenah.adjust_for_ambient_noise(source)
        listenah.energy_threshold=max(listenah.energy_threshold,min_energy_threshold)
        pass
    print("Set minimum energy threshold to {}".format(listenah.energy_threshold))

if speak:
    speaker = pyttsx.init()
    speaker.say(greeting)
    speaker.runAndWait()
    del speaker

input_txt=''
while input_txt != end_cue:
    if listen:    
        print '[Waiting for you to speak]'
        with mic as source:
            utterance = listenah.listen(source)
            pass
        input_txt = listenah.recognize_google(utterance)
        print '?> ' + input_txt
    else:
        print '[Waiting for you to type]'
        input_txt = raw_input('?> ')
        
    answer_txt = alice.respond(input_txt)
    print answer_txt

    if speak:
        speaker = pyttsx.init()
        speaker.say(answer_txt)
        speaker.runAndWait()
        del speaker

alice.saveBrain(alice_lib_root + alice_brain)