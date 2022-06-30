from cgitb import text
from email.mime import audio
import speech_recognition as sr



class SpeechRecognition():
    def __init__(self):
        self._recog = sr.Recognizer()

    def recognize_from_file(self, filename=None):
        try:
            with sr.AudioFile(filename) as source:
                audiofile = self._recog.listen(source)
                try:
                    text= self._recog.recognize_google(audiofile)
                    print(text)
                except:
                    print('Check internet connectivity')
        except:
            print('No Such File Found')

    def recognize_from_microphone(self):
        with sr.Microphone() as source:
            audio = self._recog.listen(source)
            try:
                text = self._recog.recognize_google(audio)
                print(text)
            except:
                print('Check internet connectivity')

speech_recognition = SpeechRecognition()
speech_recognition.recognize_from_file('speech.wav')
speech_recognition.recognize_from_microphone()



     
        
    

   