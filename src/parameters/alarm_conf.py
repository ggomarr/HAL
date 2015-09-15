'''
Created on Sep 11, 2015

@author: ggomarr
'''

# alarm_types
#  'julius' for Julius
#  'sphinx' for pocketsphinx
#  'shell'  for terminal

type_julius = 'julius'
type_sphinx = 'sphinx'
type_shell  = 'shell'

alarm_type = type_sphinx

# julius specific parameters

julius_conf = '/home/ggomarr/eclipse/workspace/PyAIML/src/alarm/julius/julian.jconf'
startstring = 'sentence1: <s> '
endstring = ' </s>'

# sphinx specific parameters

sphinx_lang = '/home/ggomarr/eclipse/workspace/PyAIML/src/alarm/6828/6828'
sphinx_acoustic_model = '/usr/local/share/pocketsphinx/model/en-us/en-us'
