# pip install SpeechRecognition
# brew install portaudio
# pip install pyaudio
# pip install pyttsx3


# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech


def SpeakText(command):
	# Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.languages[0] == u"en_IN":
            engine.setProperty('voice', voice.id)
            break
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

	# Exception handling to handle
	# exceptions at the runtime
    try:

		# use the microphone as source for input.
        with sr.Microphone(device_index=2) as source2:

			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
            print("start record")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("end record")

			# listens for the user's input
            print("start listen")
            audio2 = r.listen(source2, phrase_time_limit=5)
            print("end - listen")
			# Using google to recognize audio
            print("start recog")
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("end recog")

            print("Did you say ",MyText)
            SpeakText(MyText)
			
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
		
    except sr.UnknownValueError:
        print("unknown error occurred")

