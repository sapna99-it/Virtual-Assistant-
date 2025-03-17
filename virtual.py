import openai 
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import pywhatkit as kt
import subprocess
import os

# Initialize the speech engine
engine = pyttsx3.init()

# Initialize the OpenAI client
openai.api_key = "OpenAI API key"  

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Take voice input from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}")
        except Exception as e:
            print("Sorry, I could not understand. Can you repeat?")
            return "None"
        return statement.lower()

def chat_with_gpt(query):
    """Get response from OpenAI GPT model"""
    try:
        print("Sending query to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        answer = response["choices"][0]["message"]["content"]
        print("Response received from OpenAI.")
        return answer
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Sorry, I am unable to fetch a response right now."

def find_and_open_file(filename):
    """Search for a file in the system, print its location, open it, and open its folder in File Explorer"""
    # Convert the input filename to lowercase for case-insensitive comparison
    filename_lower = filename.lower()

    # Search for the file in the system
    for root, dirs, files in os.walk('C:\\'):  # Change 'C:\\' to the directory you want to search in
        for file in files:
            # Get the file name without extension
            file_name_without_ext = os.path.splitext(file)[0].lower()
            # Compare filenames without extension in a case-insensitive manner
            if file_name_without_ext == filename_lower:
                file_path = os.path.join(root, file)
                # Print the file location to the console
                print(f"File found at: {file_path}")
                # Speak the file location
                speak(f"File found at: {file_path}")
                
                # Open the folder containing the file in File Explorer
                subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)
                
                # Open the file if it's a supported type
                if file_path.endswith(('.txt', '.pdf', '.docx', '.jpg', '.png', '.mp3', '.mp4')):
                    try:
                        os.startfile(file_path)
                        speak(f"Opening {file}.")
                    except Exception as e:
                        print(f"Error opening file: {e}")
                        speak("Sorry, I couldn't open the file.")
                else:
                    speak("This file type is not supported for opening.")
                
                return
    
    # If the file is not found
    print("File not found in the system.")
    speak("File not found in the system.")

def open_application(app_name):
    """Open a system application based on user input"""
    app_name = app_name.lower()
    apps = {
        "calculator": "calc.exe",
        "weather": "msnweather:",  # Opens the Weather app in Windows
        "notepad": "notepad.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "task manager": "taskmgr.exe",
    }

    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name], shell=True)
            speak(f"Opening {app_name}.")
        except Exception as e:
            speak(f"Sorry, I couldn't open {app_name}.")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

if __name__ == "__main__":
    speak("Hello! I am Jarvis, your personal assistant.")
    
    while True:
        speak("How can I assist you?")
        statement = takeCommand()

        if "stop" in statement or "goodbye" in statement or "quit" in statement or "exit" in statement:
            speak("Goodbye! Have a great day.")
            break

        elif "wikipedia" in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif "open youtube" in statement:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")

        elif "open google" in statement:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif "tell me a joke" in statement or "joke" in statement:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif "what is" in statement or "who is" in statement or "search" in statement:
            statement = statement.replace("search", "")
            speak(f"Searching for {statement}")
            kt.search(statement)

        elif "play" in statement:
            statement = statement.replace("play", "")
            speak(f"Playing {statement} on YouTube.")
            kt.playonyt(statement)

        elif "what is" in statement or "who is" in statement or "explain" in statement:
            response = chat_with_gpt(statement)
            speak(response)
            print(response)

        elif "find file" in statement or "found file" in statement or "file" in statement:
            speak("Please tell me the name of the file you are looking for.")
            filename = takeCommand()
            if filename != "None":
                speak(f"Searching for {filename}.")
                find_and_open_file(filename)
            else:
                speak("Sorry, I did not get the file name.")

        elif "open" in statement:
            app_name = statement.replace("open", "").strip()
            open_application(app_name)

        else:
            response = chat_with_gpt(statement)
            speak(response)
            print(response)
