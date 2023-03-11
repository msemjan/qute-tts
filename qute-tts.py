#!/usr/bin/env python3
import os
from gtts import gTTS

# Get text from the environment variable
mytext = os.getenv('QUTE_SELECTED_TEXT')
  
# Language in which you want to convert
language = 'en'

# Top Level Domain
tld='co.uk'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, tld=tld, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("tmp.mp3")
  
# Playing the converted file
os.system("mpv tmp.mp3")

# Delete the temporary file after it was read
os.system("rm tmp.mp3")
