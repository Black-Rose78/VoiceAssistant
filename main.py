import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice commands
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google_cloud(voice)
            command = command.lower()
            print("You said: " + command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        talk("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        talk("Sorry, I could not connect to the service.")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("An error occurred.")
    return ""

# Function to process commands and respond
def respond(command):
    if 'hello' in command:
        talk("Hello! How can I assist you?")
    elif 'how are you' in command:
        talk("I'm an AI assistant, so I don't have feelings, but thank you for asking!")
    elif 'what is your name' in command:
        talk("I am your AI assistant.")
    elif 'bye' in command:
        talk("Goodbye! Have a nice day!")
        return False
    else:
        talk("Sorry, I don't know how to respond to that.")
    return True

# Main function to run the voice assistant
def run_voice_assistant():
    active = True
    while active:
        command = listen()
        if command:
            active = respond(command)

# Run the voice assistant
run_voice_assistant()