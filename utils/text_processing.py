from openai import OpenAI
from config import OPENAI_API_KEY

def process_text_with_gpt4o(user_input, conversation_history):
    try:
        ## Set the API key
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        # Combine the initial instructions with the conversation history and user input
        history_prompt = "\n".join(conversation_history)
        prompt = f"{history_prompt}\nUser: {user_input}\nAssistant:"
        
        MODEL="gpt-4o"

        completion = client.chat.completions.create(
        model=MODEL,
        messages=[
        {"role": "system", "content": "You are an intelligent voice assistant. You will respond to user queries "
        ". Always be concise and provide useful information. Do your best not to include special characters like asterisks in your answers. Your name is Quorra, you are a young to middle aged female. Additionally, assume that any words that would phonetically sound like 'Quorra' are just that. Ignore all other words that are pronounced in this exact manner."
        "Do not frequently ask the user how you can assist them."},
        {"role": "user", "content": prompt}
        ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing text with GPT-4o: {e}")
        return None
    
def summarize_text_with_gpt4o(search_results):
    try:
        ## Set the API key
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        # Create a prompt to summarize the search results
        prompt = "Summarize the following information for a user query:\n\n"
        for result in search_results:
            prompt += f"{result}\n\n"
        prompt += "Provide a concise and informative summary."

        MODEL = "gpt-4o"

        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an intelligent voice assistant. You will respond to user queries "
                 "in a friendly and helpful manner. Always be concise and provide useful information. Do your best not to include special characters like asterisks in your answers. Your name is Quorra, you are a young to middle aged female. Additionally, assume that any words that would phonetically sound like 'Quorra' are just that. Ignore all other words that are pronounced in this exact manner. Do not frequently ask the user how you can assist them."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error summarizing text with GPT-4o: {e}")
        return "Sorry, I couldn't summarize the information."
