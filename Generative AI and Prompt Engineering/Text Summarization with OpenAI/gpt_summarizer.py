from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to summarize text using GPT-3.5 Turbo with ChatCompletion
def summarize_text(text):
    try:
        # Make API request using ChatCompletion
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant asked to summarize texts."},
            {"role": "user", "content": f"Summarize the following text in 1000 characters or less:\n{text}"}
        ],
        temperature=0.8,
        max_tokens=250,
        stop=None)
        # Since ChatCompletion responses are structured differently, adjust extraction method
        if response.choices:
            return response.choices[0].message.content.strip()
        else:
            return "No summary provided."
    except Exception as e:  # Using a broad exception to catch any error
        # Handle errors gracefully
        return f"An error occurred: {str(e)}"

# Load text from a file
def load_text_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The file was not found."

# Main execution
if __name__ == "__main__":
    # Specify the path to your text file
    file_path = "sample-text.txt"
    
    # Load text
    text = load_text_from_file(file_path)
    
    if text.startswith("Error:"):
        print(text)  # Print error message if file is not found
    else:
        # Summarize text
        summary = summarize_text(text)
        print("Summary:", summary)
