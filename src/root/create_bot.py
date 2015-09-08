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

end_cue = 'BYE'

# End parameters

import aiml
import os.path

alice = aiml.Kernel()

if os.path.isfile(alice_lib_root + alice_brain):
    alice.loadBrain(alice_lib_root + alice_brain)
else:
    for alice_lib in alice_libs:
        alice.learn(alice_lib_root + alice_lib)
    
input_txt=''
while input_txt != end_cue:
    input_txt = raw_input('?> ')
    print alice.respond(input_txt)
    
alice.saveBrain(alice_lib_root + alice_brain)