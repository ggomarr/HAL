'''
Created on Sep 8, 2015

@author: ggomarr
'''

# Parameters

alice_lib_root = '/home/ggomarr/eclipse/workspace/PyAIML/alice/'

alice_libs = [ 'reduction?.safe.aiml',
               'reductions.update.aiml',
               'mp?.aiml' ]

#alice_libs = [ 'reduction?.safe.aiml',
#               'reductions.update.aiml',
#               'mp?.aiml',
#               '*.aiml' ]

# End parameters

import aiml

alice = aiml.Kernel()

for alice_lib in alice_libs:
    alice.learn(alice_lib_root + alice_lib)
    
