# import the library needed for the virtual assistant
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import time
import datetime
import pyjokes
from ecapture import ecapture as ec
import pywhatkit as kt
import subprocess
import smtplib
import requests

print('Loding your AI personal assistant Jarvis')
engine = pyttsx3.init()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


# now, let us obtain voice input from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...!")
        audio = r.listen(source)
        try:
            print("Recognizing")
            statement = r.recognize_google(audio, language='en-in')
            print("I heard you say " + statement)
        except Exception as e:
            print("Hey, I could not understand what you say")
            return "None"
        return statement


# the engine will then repeat what you said before performing your command
def speak(text):
    engine.say(text)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('login email id', 'password')
    server.sendmail('sender email id', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        speak("Tell me how can i help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "stop" in statement or "okay bye" in statement or "goodbye" in statement or "quit" in statement:
            speak('Your personal assistant jarvis is shutting down,Good bye')
            print('Your personal assistant jarvis is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome open now")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail website is open now")

        elif 'tell jokes' in statement or 'joke' in statement:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am jarvis version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,'
                  'predict weather'
                  'in different cities , get top headline news from times of india etc')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sapna Singh")
            print("I was built by Sapna Singh")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)


        elif 'search' in statement:
            statement = statement.replace("search", "")
            kt.search(statement)
            # webbrowser.open(statement)
            time.sleep(5)

        elif 'play' in statement:
            statement = statement.replace("play", "")
            # ebbrowser.open(f'https://open.spotify.com/search/{statement}')
            # time.sleep(13)
            engine.say("playing" + statement)
            engine.runAndWait()
            kt.playonyt(statement)
            # time.sleep(120)
            break
            # engine.runAndWait()
            # pyautoqui.click(x=1055, y=617)
            # speak('Playing' + song)

        elif "open calculator" in statement:
            speak("Calculator opening...")
            subprocess.Popen(['open', '-a', 'Calculator'])

        elif 'email to sapna' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sapanasingh1999@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry . I am not able to send this email")

        elif "open camera" in statement:
            speak(" Camera opening...")
            subprocess.Popen(['open', '-a', 'Photo Booth'])

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif "open map" in statement:
            speak(" Map is opening...")
            subprocess.Popen(['open', '-a', 'Maps'])

        elif "open calender" in statement:
            speak(" Calender opening...")
            subprocess.Popen(['open', '-a', 'Calendar'])

        elif "open mail" in statement or "open mail app" in statement:
            speak(" Mail is opening...")
            subprocess.Popen(['open', '-a', 'Mail'])

        elif "weather" in statement or "tell weather" in statement or "climate" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) + "\n humidity in percentage is " + str(
                    current_humidiy) + "\n description  " + str(weather_description))
                print(" Temperature in kelvin unit = " + str(
                    current_temperature) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "i love you" in statement:
            speak("Thank you! But, It's a pleasure to hear it from you.")

        elif "write a note" in statement:
            speak("What should i write, madam")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "how are you" in statement:
            speak("I am fine")

        elif "what is the fees of MCA course" in statement:
            speak("42000 Rupees")

        elif "placement detail" in statement or "tell about a placement detail" in statement:
            speak('Placements for our batch and the seniors batch were not at all good. None of our college friends '
                  'was placed through the college. About 20% of students got internships from the college. The '
                  'highest stipend offered was Rs 18,000 for 6 months, and the lowest was a free internship. There is '
                  'a placement cell in the college, but its not useful enough.')

        elif "tell me about college infrastructure" in statement:
            speak('The facilities of the college are amazing. We had Wi-Fi all over the campus. Its a 100 acres '
                  'campus with all the facilities. The college has 2 football/cricket grounds, swimming pool, '
                  'and inhouse medical facilities. As there is hotel management on the campus, we had a mini hotel '
                  'kind of a canteen and had a variety of dishes available in the canteen. I did not face any '
                  'infrastructure related issues during my college time.')

        elif "founder of dy patil" in statement:
            speak('Ajeenkya D Y Patil was born in Mumbai, the son of Pushpalata Patil and D. Y. Patil, a Padma Shri '
                  'recipient, and founder of the D Y Patil Group.')

        elif "tell about faculty member of mca" in statement:
            speak('Prof. Ashok Deokar Assistant Professor and Head Of Department in MCA'
                  'Prof. Sapna Chavan Assistant Professor'
                  'Prof. Shubham Wadpalliwar Assistant Professor'
                  'Dr Jayshri Patil    Assistant Professor '
                  'Prof. Santosh S. Deshmukh Assistant Professor'
                  'Prof. Hidayat Pirjade Assistant Professor'
                  'Prof. Urmila Kadam Assistant Professor'
                  'Prof. Asmita Hendre Assistant Professor '
                  'Prof. Ravikant D. Kale Assistant Professor '
                  'Mrs. Ashwini Dolas Librarian')

        elif "what is mca" in statement:
            speak('M.C.A (Master of Computer Application ) is generally a 3-year post graduate degree / diploma in '
                  'Computer Applications. In some institutes it is called PGDCA, PGDIT etc.')

        elif "what is the eligibility criteria for mca course" in statement:
            speak('Bachelor Degree of 3 years duration and should have studied Maths / Stats / Business Stats / '
                  'Computer Science / Computer Programming either at degree level or 10+2 level with Minimum 50% '
                  'marks in aggregate of all the years of degree examination.')

        elif "mca course duration" in statement:
            speak('2 years')

        elif "what are the subjects in mca" in statement:
            speak('MCA subjects include topics like java,data structure,networking,advance web technology,python,'
                  'Artifical intelligence,Android,software testing,cloud computing etc ')
            
        elif "tell about hostel" in statement:
            speak('Hostel Fee Details:Minimum amount as per room being availed, before leaving the Hostel.(a) '
                  'Standard Rooms - Rs. 50,000 (b)Premium Rooms - Rs. 60,000 (c)Premium Plus Rooms - Rs. 80,'
                  '000 (d) Supreme Rooms - Rs. 90,000')
# import the library needed for the virtual assistant
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import time
import datetime
import pyjokes
from ecapture import ecapture as ec
import pywhatkit as kt
import subprocess
import smtplib
import requests

print('Loding your AI personal assistant Jarvis')
engine = pyttsx3.init()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


# now, let us obtain voice input from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...!")
        audio = r.listen(source)
        try:
            print("Recognizing")
            statement = r.recognize_google(audio, language='en-in')
            print("I heard you say " + statement)
        except Exception as e:
            print("Hey, I could not understand what you say")
            return "None"
        return statement


# the engine will then repeat what you said before performing your command
def speak(text):
    engine.say(text)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('miremote1999@gmail.com', 'sap12345')
    server.sendmail('sapanasingh1999@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        speak("Tell me how can i help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "stop" in statement or "okay bye" in statement or "goodbye" in statement or "quit" in statement:
            speak('Your personal assistant jarvis is shutting down,Good bye')
            print('Your personal assistant jarvis is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome open now")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail website is open now")

        elif 'tell jokes' in statement or 'joke' in statement:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am jarvis version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,'
                  'predict weather'
                  'in different cities , get top headline news from times of india etc')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sapna Singh")
            print("I was built by Sapna Singh")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)


        elif 'search' in statement:
            statement = statement.replace("search", "")
            kt.search(statement)
            # webbrowser.open(statement)
            time.sleep(5)

        elif 'play' in statement:
            statement = statement.replace("play", "")
            # ebbrowser.open(f'https://open.spotify.com/search/{statement}')
            # time.sleep(13)
            engine.say("playing" + statement)
            engine.runAndWait()
            kt.playonyt(statement)
            # time.sleep(120)
            break
            # engine.runAndWait()
            # pyautoqui.click(x=1055, y=617)
            # speak('Playing' + song)

        elif "open calculator" in statement:
            speak("Calculator opening...")
            subprocess.Popen(['open', '-a', 'Calculator'])

        elif 'email to sapna' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sapanasingh1999@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry . I am not able to send this email")

        elif "open camera" in statement:
            speak(" Camera opening...")
            subprocess.Popen(['open', '-a', 'Photo Booth'])

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif "open map" in statement:
            speak(" Map is opening...")
            subprocess.Popen(['open', '-a', 'Maps'])

        elif "open calender" in statement:
            speak(" Calender opening...")
            subprocess.Popen(['open', '-a', 'Calendar'])

        elif "open mail" in statement or "open mail app" in statement:
            speak(" Mail is opening...")
            subprocess.Popen(['open', '-a', 'Mail'])

        elif "weather" in statement or "tell weather" in statement or "climate" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) + "\n humidity in percentage is " + str(
                    current_humidiy) + "\n description  " + str(weather_description))
                print(" Temperature in kelvin unit = " + str(
                    current_temperature) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "i love you" in statement:
            speak("Thank you! But, It's a pleasure to hear it from you.")

        elif "write a note" in statement:
            speak("What should i write, madam")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "how are you" in statement:
            speak("I am fine")

        elif "what is the fees of MCA course" in statement:
            speak("42000 Rupees")

        elif "placement detail" in statement or "tell about a placement detail" in statement:
            speak('Placements for our batch and the seniors batch were not at all good. None of our college friends '
                  'was placed through the college. About 20% of students got internships from the college. The '
                  'highest stipend offered was Rs 18,000 for 6 months, and the lowest was a free internship. There is '
                  'a placement cell in the college, but its not useful enough.')

        elif "tell me about college infrastructure" in statement:
            speak('The facilities of the college are amazing. We had Wi-Fi all over the campus. Its a 100 acres '
                  'campus with all the facilities. The college has 2 football/cricket grounds, swimming pool, '
                  'and inhouse medical facilities. As there is hotel management on the campus, we had a mini hotel '
                  'kind of a canteen and had a variety of dishes available in the canteen. I did not face any '
                  'infrastructure related issues during my college time.')

        elif "founder of dy patil" in statement:
            speak('Ajeenkya D Y Patil was born in Mumbai, the son of Pushpalata Patil and D. Y. Patil, a Padma Shri '
                  'recipient, and founder of the D Y Patil Group.')

        elif "tell about faculty member of mca" in statement:
            speak('Prof. Ashok Deokar Assistant Professor and Head Of Department in MCA'
                  'Prof. Sapna Chavan Assistant Professor'
                  'Prof. Shubham Wadpalliwar Assistant Professor'
                  'Dr Jayshri Patil    Assistant Professor '
                  'Prof. Santosh S. Deshmukh Assistant Professor'
                  'Prof. Hidayat Pirjade Assistant Professor'
                  'Prof. Urmila Kadam Assistant Professor'
                  'Prof. Asmita Hendre Assistant Professor '
                  'Prof. Ravikant D. Kale Assistant Professor '
                  'Mrs. Ashwini Dolas Librarian')

        elif "what is mca" in statement:
            speak('M.C.A (Master of Computer Application ) is generally a 3-year post graduate degree / diploma in '
                  'Computer Applications. In some institutes it is called PGDCA, PGDIT etc.')

        elif "what is the eligibility criteria for mca course" in statement:
            speak('Bachelor Degree of 3 years duration and should have studied Maths / Stats / Business Stats / '
                  'Computer Science / Computer Programming either at degree level or 10+2 level with Minimum 50% '
                  'marks in aggregate of all the years of degree examination.')

        elif "mca course duration" in statement:
            speak('2 years')

        elif "what are the subjects in mca" in statement:
            speak('MCA subjects include topics like java,data structure,networking,advance web technology,python,'
                  'Artifical intelligence,Android,software testing,cloud computing etc ')
            
        elif "tell about hostel" in statement:
            speak('Hostel Fee Details:Minimum amount as per room being availed, before leaving the Hostel.(a) '
                  'Standard Rooms - Rs. 50,000 (b)Premium Rooms - Rs. 60,000 (c)Premium Plus Rooms - Rs. 80,'
                  '000 (d) Supreme Rooms - Rs. 90,000')
