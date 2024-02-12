# GPT-3.5 Turbo Planet Generator

This Python script utilizes the GPT-3.5 Turbo model from OpenAI to generate unique and fictional names for planets, along with descriptions for each planet type.

## Setup

1. Clone this repository to your local machine.

## Retrieving OpenAI API Key


1. **Sign Up/Login to OpenAI**:
   - If you don't already have an account, visit the OpenAI website at [openai.com](https://openai.com) and sign up for an account. If you have an account, log in using your credentials.

2. **Navigate to API Section**:
   - Once logged in, navigate to the API section of the OpenAI website. You can usually find this in the main menu or dashboard.

3. **Request API Access**:
   - Look for the option to request API access or generate an API key. Click on it to proceed.

4. **Provide Necessary Information**:
   - Fill out any required forms or fields with accurate information. This may include details about your intended use case or project.

5. **Receive API Key**:
   - Once your request is approved, you'll receive your API key. This key is typically provided in the form of a string of alphanumeric characters.

6. **Secure Your API Key**:
   - Keep your API key secure and avoid sharing it publicly. Treat it like a password and store it securely. Avoid hardcoding it directly into your code.

7. **Start Using the API**:
   - You can now use your OpenAI API key to access the available APIs and integrate them into your applications. Refer to the OpenAI documentation for guidance on how to use the API effectively.


2. Install the required Python packages using pip3:

```
pip3 install openai python-dotenv
```
  Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

3. Create a `.env` file in the project directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

4. Run the script:

```
python3 planet_generator.py
```

## Description

The script interacts with the GPT-3.5 Turbo model through the OpenAI API to generate names and descriptions for fictional planets. It first prompts the model to generate a specified number of unique planet names. Then, it pairs each generated name with a randomly selected planet type (Gas Giant, Moon, or Rogue Planet). Finally, it prompts the model to generate a random description for each planet, ensuring that each description consists of exactly two sentences.

## Usage

Modify the `planet_names_prompt` variable to specify the number of unique planet names you want to generate.

```python
planet_names_prompt = "Generate 3 unique and fictional names for planets."
```

Adjust the `planet_types` list to include the types of planets you want to generate descriptions for.

```python
planet_types = ['Gas Giant', 'Moon', 'Rogue Planet']
```

Run the script and observe the generated planet names and descriptions printed to the console.


## Contributing

Your contributions are welcome! If you have suggestions for improving the script or have found a bug, please open an issue or a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
