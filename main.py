from utils.audio_input import get_audio_input
from utils.text_processing import process_text_with_gpt4o, summarize_text_with_gpt4o
from utils.text_to_speech import text_to_speech_with_google
from utils.web_search import search_web
from utils.image_generation import generate_image, save_and_open_image
from config import DEFAULT_VOICE_NAME
import keyboard

def main(voice_name=DEFAULT_VOICE_NAME):
    conversation_history = []  # Initialize conversation history

    while True:
        user_input = get_audio_input()
        
        if user_input:
            conversation_history.append(f"User: {user_input}")
            
            if "search" in user_input.lower():
                search_query = user_input.lower().replace("search", "").strip()
                search_results = search_web(search_query)
                summarized_results = summarize_text_with_gpt4o(search_results)
                response_text = summarized_results
            elif "generate image with prompt" in user_input.lower():
                    image_prompt = user_input.lower().replace("generate image with prompt", "").strip()
                    image = generate_image(image_prompt)
                    if image:
                        save_and_open_image(image)
                    response_text = f"Image generation complete for prompt: {image_prompt}"
            else:
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
