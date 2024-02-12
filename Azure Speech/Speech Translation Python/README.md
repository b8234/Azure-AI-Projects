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
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Speech/Speech\ Translation\ Python/translator
```

Run command to install packages:

```
pip3 install python-dotenv azure-cognitiveservices-speech playsound
```

Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### Provision an Azure AI Speech Resource

Azure AI Speech includes a speech translation API that allows you to translate spoken language. Follow these steps to provision an Azure AI Speech resource:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com) and sign in with your Microsoft account associated with your Azure subscription.
2. In the search field at the top, search for "Azure AI services" and press Enter.
3. Under the results, select Create under "Speech service".
4. Configure the resource with the following settings:
   - Subscription: Your Azure subscription.
   - Resource group: Choose or create a resource group.
   - Region: Choose any available region.
   - Name: Enter a unique name.
   - Pricing tier: Select F0 (free) or S (standard) if F is not available.
   - Responsible AI Notice: Agree.
5. Select Review + create.
6. Wait for deployment to complete, and then go to the deployed resource.
7. View the Keys and Endpoint page. You will need the information on this page later in the exercise.

### Create an .env file to store credentials

- Add a `.env` file with Azure service credentials:
  ```
  SPEECH_KEY=your_speech_service_key
  SPEECH_REGION=your_speech_service_region
  ```

## How to Use
Run the script and follow the prompts to speak in English. Choose the target language for translation:

```
python3 translator.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained practical skills in implementing real-time speech translation using Azure Speech services.
- Developed proficiency in creating applications that facilitate multi-lingual interactions.
- Enhanced understanding of applying conversational AI in a global context.

## Acknowledgments
This project was inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
