# Azure AI Text Translation Project

## Description
This project is part of the Microsoft AI MS Learn series. It uses Azure AI's Text Translation service. The Python script enables dynamic language translation, allowing users to input text and translate it into a chosen target language. It also supports language detection and lists available translation languages.

## Objectives
- Leverage Azure AI's Text Translation service for real-time text translation.
- Implement language detection and user-driven translation into various languages.
- Showcase the practical application of Azure AI in building language translation systems.

## Technologies Used
- Azure AI Translation Text Service for real-time text translation.
- Python for creating an interactive translation application.
- Azure SDK to facilitate communication with Azure Text Translation services.

## Setup and Installation
To set up this project:

```
git clone <repository-url>
cd <project-directory>
pip install azure-ai-translation-text
```

## Configuration
- Set up Azure Translation resources in Azure.
- Add a `.env` file with Azure service credentials:
  ```
  TRANSLATOR_KEY=your_translator_key
  TRANSLATOR_REGION=your_translator_region
  ```

## How to Use
Run the script and follow the prompts to input text for translation and select a target language:

```
python script_name.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained practical experience in using Azure AI services for language translation.
- Developed skills in creating interactive applications using Azure's cognitive services.
- Enhanced understanding of real-world applications of AI in overcoming language barriers.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).
