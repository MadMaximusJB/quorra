from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os
import platform
import subprocess
from config import OPENAI_API_KEY

def generate_image(prompt):
    try:
        # Set the API key
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.images.generate(
            prompt=prompt,
            n=1,
            size="1024x1024",
            model="dall-e-3",
        )
        
        # Access the URL from the response object
        image_url = response.data[0].url
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        return image
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def save_and_open_image(image, file_path='generated_image.png'):
    try:
        image.save(file_path)
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Linux":
            subprocess.call(["xdg-open", file_path])
        else:
            print(f"Opening images is not supported on this platform: {platform.system()}")
    except Exception as e:
        print(f"Error saving or opening image: {e}")
