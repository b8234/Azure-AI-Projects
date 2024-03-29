# DALL-E 3 Image Generation

This Python script allows users to generate images based on textual prompts using OpenAI's DALL-E 3 model. It leverages the OpenAI API to create an image, which is then downloaded and saved locally.

## Features

- **Generate Images**: Create images from text prompts using OpenAI's advanced DALL-E 3 model.
- **Error Handling**: Includes basic error handling for API requests and image saving.
- **Environment Variables**: Utilizes environment variables for API key management, enhancing security.

## Prerequisites

Before running this script, ensure you have the following:

- Python 3.6 or later.
- An OpenAI API key with access to the DALL-E 3 model.
- The `openai`, `requests`, and `Pillow` Python packages installed.

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

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/b8234/Azure-AI-Projects.git
   cd Azure-AI-Projects/Generative\ AI\ and\ Prompt\ Engineering/DALL-E\ 3
   ```

2. **Install Dependencies**:

   ```bash
   pip3 install openai requests Pillow python-dotenv
   ```
   Or install the required dependencies via requirements, run the following command:
   
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

To run the script, navigate to the project directory and execute:

   ```bash
   python3 generate_image.py
   ```

Follow the prompt to enter a description of the image you wish to generate. The script will handle the generation and saving process, notifying you of the outcome.

## Error Handling

The script includes basic error handling for common issues, such as API request failures and image download problems. If an error occurs, it will print a descriptive message to the console.

## Customization

You can customize the script by modifying the `model`, `size`, and `quality` parameters in the `generate_image` function call to suit your specific needs.

## Contributing

Your contributions are welcome! If you have suggestions for improving the script or have found a bug, please open an issue or a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
