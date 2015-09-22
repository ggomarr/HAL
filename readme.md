## HAL - The Dawn Of The Algorithm

This project is just a proof of concept for a voice based computer interface. It uses a combination of Google Speech Recognition, pocketsphinx, and julius to interpret speech and Google Text To Speech and pyttsx to speak back. There is a shell fallback also, just in case.

The interface can do the following:

- Sing 'Daisy, Daisy, give me an answer, do...'
- Look for information in Wikipedia
- Control the Plex Media Server
- Call the Police
- Chitchat

The framework is flexible enough for other actions to be incorporated with relative ease.

## Description

HAL has two operating modes:

- Inactive: in this mode, HAL will listen to specific commands that will wake the interface up. Those commands are:

	- Okay HAL
	- HAL, wake up
	- HAL, are you there?
	- HAL, can you help me?
	- HAL, do you have a minute?
	
	From inactive mode, the command 'HAL, shut down' can be issued in order to completely shut down the HAL interface.

- Active: in this mode, HAL pushes the input through a layer of interpretation based on regex matching. If a command can be identified, it gets executed; otherwise, the input gets sent to the chatbot, based on A.L.I.C.E.

	Samples of Wikipedia commands would be:
	- What can you gather about little green men from wikipedia?
	- Would you be kind enough to get me a summary on Chernobyl?
	- Do you know anything about banjos?

	Samples of Plex commands would be:
	- Can you play 'The Big Bang Theory'?
	- Play 'Dead Man'
	- HAL, pause Plex
	- Stop the movie
	
	To put HAL back into inactive mode, the following commands can be used:

	- Goodbye!
	- Go to sleep
	- See you later!
	- That is all for now

## Requirements

In order to work, the following needs to be available in the target system:

- Pocketsphinx, Julius

	Some paths related to these will need to be updated in the configuration file /parameters/alarm_conf.py.

- Python packages:

	- subprocess, re, random, requests, tempfile, os
	- pyaudio, pocketsphinx, speech_recognition, gtts, pyttsx, aiml, plexapi, wikipedia
	
## Collaboration

I cannot promise anything, but do not hesitate getting in touch if you have questions or comments!