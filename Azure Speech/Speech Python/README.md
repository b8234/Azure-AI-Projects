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

To install the required dependencies, run the following command:

```bash
pip3 install -r requirements.txt
```


## Configuration
- Set up Azure Speech services in the Azure portal.
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
