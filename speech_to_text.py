import speech_recognition as sr
from gtts import gTTS

def speech_to_text():

    # Get audio input from microphone
    r = sr.Recognizer()

    # Set up the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    speech_to_text()
