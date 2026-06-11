import pyttsx3
import datetime

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Welcome message
speak("Hello Rahul!")
speak("I am your Python Assistant. How can I help you today?")

# Main loop
while True:
    command = input("Enter command: ").lower()

    if command == "hello":
        speak("Hello, how are you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + current_time)

    elif command == "date":
        today = datetime.date.today()
        speak("Today's date is " + str(today))

    elif command == "your name":
        speak("My name is Python Assistant")

    elif command == "exit":
        speak("Goodbye Rahul!")
        break

    else:
        speak("Command not recognized")