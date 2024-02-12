# Azure Speech Recognition and Synthesis Project

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure Cognitive Services Speech SDK. It focuses on implementing speech recognition to understand spoken commands and speech synthesis to respond orally. The script is set up to recognize the question "What time is it?" and respond with the current time.

## Objectives
- Utilize Azure Speech SDK for recognizing spoken language.
- Implement speech synthesis to convert text responses into spoken language.
- Demonstrate the integration of Azure speech services in a Python application for interactive voice response.

## Technologies Used
- Azure Cognitive Services Speech SDK for speech recognition and synthesis.
- Python for scripting and orchestrating speech interactions.
- `playsound` library for playing synthesized speech (if applicable).

## Setup and Installation
To set up this project:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Speech/Speech\ Python/speaking-clock
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

Azure AI Speech is a service that provides speech-related functionality, including speech-to-text and text-to-speech APIs. Follow these steps to provision an Azure AI Speech resource:

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

### Create .env file to store credentials

- Create a `.env` file with the necessary Azure service details:
  ```
  SPEECH_KEY=your_speech_service_key
  SPEECH_REGION=your_speech_service_region
  ```

## How to Use
Run the script, speak the command "What time is it?", and listen to the spoken response:

```
python3 speaking-clock.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained practical experience with Azure Speech services, including both speech-to-text and text-to-speech capabilities.
- Developed skills in creating applications that can interact with users through voice.
- Enhanced understanding of real-time speech processing and response generation using Azure's cognitive services.

## Acknowledgments
This project was inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
