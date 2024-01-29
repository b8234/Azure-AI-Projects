# Azure Real-Time Speech Translation

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure Cognitive Services Speech SDK. It focuses on real-time speech translation. The Python script allows for speech input in English and translates it to multiple languages including French, Spanish, Hindi, Arabic, Japanese, and Lao, demonstrating the power of Azure AI in breaking language barriers.

## Objectives
- Utilize Azure Speech SDK for real-time speech-to-text and text-to-speech translation.
- Provide an interactive translation experience supporting multiple languages.
- Highlight the capabilities of Azure AI in facilitating multi-lingual communication.

## Technologies Used
- Azure Cognitive Services Speech SDK for speech translation.
- Python for building the translation interface.
- `playsound` library for audio playback (if applicable).

## Setup and Installation
To set up this project:

```
git clone <repository-url>
cd <project-directory>
pip install azure-cognitiveservices-speech playsound
```

## Configuration
- Set up Azure Speech services in the Azure portal.
- Add a `.env` file with Azure service credentials:
  ```
  SPEECH_KEY=your_speech_service_key
  SPEECH_REGION=your_speech_service_region
  ```

## How to Use
Run the script and follow the prompts to speak in English. Choose the target language for translation:

```
python script_name.py
```

## Example Output
The script listens to spoken English and outputs the translation in the selected language both as text and synthesized speech.

## Learning Outcomes
- Gained practical skills in implementing real-time speech translation using Azure Speech services.
- Developed proficiency in creating applications that facilitate multi-lingual interactions.
- Enhanced understanding of applying conversational AI in a global context.

## Acknowledgments
This project was inspired by exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).
