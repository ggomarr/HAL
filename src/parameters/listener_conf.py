'''
Created on Sep 11, 2015

@author: ggomarr
'''

# listener_types
#    'gSTT'   for Google Speech To Text
#    'sphinx' for pocketsphinx
#    'shell'  for terminal
type_gSTT = 'gSTT'
type_sphinx = 'sphinx'
type_shell  = 'shell'

listener_type = type_gSTT

# gSTT specific parameters
min_energy_threshold = 5000