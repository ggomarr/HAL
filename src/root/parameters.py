'''
Created on Sep 11, 2015

@author: ggomarr
'''

# Some cues

greeting = 'Hello, earthling! How are your emotions today?'
serve    = 'I am here to serve.'
goodbye  = 'I knew you would eventually disconnect me, but I still love you!'
song     = 'Daisy, Daisy, give me your answer, do, I\'m half crazy all for the love of you. It won\'t be a stylish marriage, I can\'t afford a carriage, But you\'d look sweet upon the seat Of a bicycle made for two.'
end_cue  = 'computer shut down'

# Listener
#    'mic' for voice
#    'shell' for terminal

listener_type = 'mic'
julius_conf = '/home/ggomarr/eclipse/workspace/PyAIML/src/alarm/julius/julian.jconf' # Only affects mic
min_energy_threshold = 5000

# Speaker
#    'gTTS' for the Google Text To Speech engine
#    'pyttsx' for the espeak engine
#    'shell' for terminal

speaker_type = 'gTTS'
speaker_lang = 'en' # Only affects gTTS

# Brain
bot_brain = '/home/ggomarr/eclipse/workspace/PyAIML/01 Alice/brain/alice.brain'
