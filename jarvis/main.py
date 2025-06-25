import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests
def processcommands(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open github" in command:
        webbrowser.open("https://github.com/") 
    elif command.lower().startswith("play"):
        song=command.split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)


    elif "news" in command:
        key = "f83d1c832887497286555e0db37ff1a2"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"

        try:
            response = requests.get(url)
            news_data = response.json()

            articles = news_data.get("articles")
            if articles:
                speak("Here are the top news headlines.")
                for i, article in enumerate(articles[:5], start=1):
                    speak(f"Headline {i}: {article['title']}")
            else:
                speak("Sorry, I couldn't find any news.")
        except Exception as e:
            speak("There was an error fetching the news.")
            print("Error:", e)


    else:
         # integrating with open ai

         print("i can only open google, youtube, github and play music from my library")
# def aiProcess(command):
#     client = OpenAI(api_key="",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content         
def aiProcess(command):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:  # safely accessing mic
            print("Listening......")
            audio = r.listen(source, timeout=3, phrase_time_limit=2)

        print("RECOGNIZING....")
        word = r.recognize_google(audio)  # you can change this to recognize_sphinx(audio)
        print("You said:", word)

        if word.lower() == "jarvis":
            speak("Yes sir, how can I help you?")
        # FUNCTIONALITY FOR ANOTHER COMMANDS AFTER JARVIS
        with sr.Microphone() as source:  # safely accessing mic
            print("ACTIVATED SUCCESFULLY......")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print("COMMAND IS :", command)
            processcommands(command.lower())

    except sr.UnknownValueError:
        print("Could not understand audio")
    except Exception as e:
        print("Error: {0}".format(e))
