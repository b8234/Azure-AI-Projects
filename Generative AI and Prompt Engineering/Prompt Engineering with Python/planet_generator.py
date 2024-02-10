from openai import OpenAI
from dotenv import load_dotenv
import os
import random

# Load environment variables
load_dotenv()

# Initialize OpenAI API client with the API key from the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[
                                                      {"role": "system", "content": "You are a creative assistant."},
                                                      {"role": "user", "content": prompt}
                                                  ])
        # Ensure the response is successfully received
        if response and response.choices:
            return response.choices[0].message.content.strip()
        else:
            return "Response was not received properly."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Modify the prompt for clarity and specificity
planet_names_prompt = "Generate 3 unique and fictional names for planets."
planet_names_response = chat_with_gpt(planet_names_prompt)

# Process the response to ensure it's in the expected format
planet_names = planet_names_response.split('\n') if '\n' in planet_names_response else [planet_names_response]

# List of planet types to pair with generated names
planet_types = ['Gas Giant', 'Moon', 'Rogue Planet']

# Randomly pair planet names with types and generate random descriptions for each pair
random.shuffle(planet_names)
for planet_name, planet_type in zip(planet_names, planet_types):
    description_prompt = f"Generate a random description for {planet_name}, the {planet_type}."
    description = chat_with_gpt(description_prompt)
    # Split the description into two sentences
    sentences = description.split('. ')[:2]
    # Join the sentences with a period and print
    print(f"{planet_name}, the {planet_type}:")
    print("Description:")
    print(". ".join(sentences).strip() + ".\n")
