from gtts import gTTS
import os



def text_to_speech(mytext,language):
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("start welcome.mp3")


if __name__ == "__main__":
    text="hello kase hai aap."
    lang="hi"
    text_to_speech(text,lang)
