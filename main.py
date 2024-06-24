from utils.audio_input import get_audio_input
from utils.text_processing import process_text_with_gpt4o
from utils.text_to_speech import text_to_speech_with_google
from config import DEFAULT_VOICE_NAME
import keyboard

def main(voice_name=DEFAULT_VOICE_NAME):
    conversation_history = []  # Initialize conversation history

    while True:
        user_input = get_audio_input()
        
        if user_input:
            conversation_history.append(f"User: {user_input}")
            response_text = process_text_with_gpt4o(user_input, conversation_history)
            
            if response_text:
                conversation_history.append(f"Quorra: {response_text}")
                print(f"Quorra: {response_text}")
                text_to_speech_with_google(response_text, voice_name=voice_name)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting Quorra.")
