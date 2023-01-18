import os
import openai

openai.organization = "org-suTf2NBidIX4WHsJYzbuwbME"
file = open("/home/pi/Desktop/openai.txt")
openai.api_key = file.readline().strip()
openai.Model.list()

# pip install SpeechRecognition
# brew install portaudio
# pip install pyaudio
# pip install pyttsx3


# Python program to translate
# speech to text and text to speech

import os
os.environ['PA_ALSA_PLUGHW']='1'

import speech_recognition as sr
from gtts import gTTS
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init("espeak")

# Function to convert text to
# speech

engine.setProperty('rate', 200)
engine.setProperty('volume', 1)
engine.setProperty('voice', "en-us")

def SpeakText(command):
	# Initialize the engine
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

	# Exception handling to handle
	# exceptions at the runtime
    try:

		# use the microphone as source for input.
        #device_index=2
        with sr.Microphone() as source2:

			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

			# listens for the user's input
            audio2 = r.listen(source2, phrase_time_limit=5)
			# Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()


            #Query the API
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=MyText,
            temperature=0,
            max_tokens=150,

            )
            print(f"you said: {MyText}")
            print(f"response:")
            query = response.choices[0].text
            query = query.replace("John", "Baymax")
            print(query)
            SpeakText(query)

    except sr.RequestError as e:
        print()
        #print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        #print("unknown error occurred")
        print()
