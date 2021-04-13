import speech_recognition as sr

def obtain_audio():

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        
def gsr():
        # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    
        
def iw():
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")

def get_speech():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		
		try:
#			print("Recording for 60 seconds")
			audio_data = recognizer.listen(source,  timeout=180)
#			print("Done recording")
	
	
	
			print("Recognizing...")
			# convert speech to text
			text = recognizer.recognize_google(audio_data)
			return text
		except:
			return "bye"


