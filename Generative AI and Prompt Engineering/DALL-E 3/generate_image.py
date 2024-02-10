from openai import OpenAI
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_image(prompt, model="dall-e-3"):
    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        # Accessing the URL of the first image in the response
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"An error occurred during image generation: {e}")
        return None

def save_image_from_url(url, file_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(file_path)
            print(f"Image saved to {file_path}")
        else:
            print(f"Failed to download the image. HTTP Status: {response.status_code}")
    except (requests.RequestException, UnidentifiedImageError) as e:
        print(f"An error occurred during image downloading/saving: {e}")

def main():
    prompt = input("Enter your prompt (up to 100 characters): ")
    if len(prompt) > 100:
        print("Error: Your prompt exceeds the 100-character limit.")
        return
    
    # Ensure the "Saved Images" folder exists
    save_folder = "Saved Images"
    os.makedirs(save_folder, exist_ok=True)

    # Generate a unique filename using the current timestamp and include the folder in the path
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(save_folder, f"generated_image_{timestamp}.jpg")

    image_url = generate_image(prompt)
    if image_url:
        save_image_from_url(image_url, file_path)
    else:
        print("Image generation was unsuccessful. Please try again with a different prompt or check for any issues.")

if __name__ == "__main__":
    main()
