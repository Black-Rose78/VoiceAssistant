```markdown
# Voice Assistant

This project is a simple voice assistant that listens to voice commands and responds using text-to-speech. It uses the `speech_recognition` library for recognizing speech and the `pyttsx3` library for text-to-speech conversion.

## Features
- Speech Recognition: Listens to voice commands using the microphone.
- Text-to-Speech: Responds to commands using a text-to-speech engine.
- Basic Command Processing: Recognizes and responds to a few basic commands.

## Requirements
- Python 3.x
- `speech_recognition` library
- `pyttsx3` library

## Setup
1. **Clone the Repository:**
    sh
    git clone https://github.com/Black-Rose78/VoiceAssistant.git
    cd voice-assistant
    

2. **Install Required Libraries:**
    sh
    pip install speechrecognition pyttsx3
    

3. **Run the Voice Assistant:**
    ```sh
    python voice_assistant.py
    ```

## Usage
- The voice assistant will start listening for commands once the script is run.
- It can recognize and respond to the following commands:
  - "hello"
  - "how are you"
  - "what is your name"
  - "bye"

### Example Commands
- **Hello**
  - You: "hello"
  - Assistant: "Hello! How can I assist you?"
- **How are you**
  - You: "how are you"
  - Assistant: "I'm an AI assistant, so I don't have feelings, but thank you for asking!"
- **What is your name**
  - You: "what is your name"
  - Assistant: "I am your AI assistant."
- **Bye**
  - You: "bye"
  - Assistant: "Goodbye! Have a nice day!" (The assistant will then stop running.)

## Code Overview

### Initialization
The recognizer and the text-to-speech engine are initialized:
```python
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
```

### Text-to-Speech Function
The `talk` function converts text to speech:
```python
def talk(text):
    engine.say(text)
    engine.runAndWait()
```

### Listen Function
The `listen` function listens to voice commands using the microphone and converts them to text:
```python
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("Listening....")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_sphinx(voice)
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
```

### Command Response Function
The `respond` function processes commands and responds accordingly:
```python
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
```

### Main Function
The `run_voice_assistant` function runs the voice assistant in a loop:
```python
def run_voice_assistant():
    active = True
    while active:
        command = listen()
        if command:
            active = respond(command)

run_voice_assistant()
```

## Troubleshooting
- **Microphone Issues:** Ensure your microphone is properly connected and configured.
- **Speech Recognition Errors:** If the assistant frequently misunderstands commands, try adjusting the microphone sensitivity or minimizing background noise.
- **Dependencies:** Ensure all required libraries are installed correctly.

---

Feel free to customize this voice assistant or expand its capabilities by adding more commands and responses. Contributions are welcome!
```
