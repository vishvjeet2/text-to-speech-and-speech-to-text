import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os
import speech_recognition as sr

# Function to handle button click
def on_button_click(button_name):
    if button_name == "Button 1":
        user_input = entry.get()
        text_to_speech(user_input, 'hi')  # Call the text_to_speech function with user input and language
        messagebox.showinfo("Button Clicked", f"{button_name} was clicked!\nYou entered: {user_input}")
    elif button_name == "Button 2":
        recognized_text = speech_to_text()  # Call the speech_to_text function and get the recognized text
        output_label.config(text="Recognized Text: " + recognized_text)  # Update the output label with the recognized text

# Function to convert text to speech
def text_to_speech(text, language):
    # Create gTTS object with provided text and language
    myobj = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio to a file named "output.mp3"
    myobj.save("output.mp3")

    # Play the audio file
    os.system("start output.mp3")

# Function to convert speech to text
def speech_to_text():
    # Get audio input from microphone
    r = sr.Recognizer()

    # Set up the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        recognized_text = r.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x300")  # Set the window size to 400x300 pixels

# Create and place the text entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create and place Button 1
button1 = tk.Button(root, text="Text to Speech", command=lambda: on_button_click("Button 1"))
button1.pack(pady=5)

# Create and place Button 2
button2 = tk.Button(root, text="Speech to Text", command=lambda: on_button_click("Button 2"))
button2.pack(pady=5)

# Create label for output
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Start the main loop
root.mainloop()
