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
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Language/Translate\ Language\ Python/translate-text
```

**Install Dependencies**:

```bash
pip3 install python-dotenv azure-ai-translate
```
Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### Provision an Azure AI Translator Resource

Azure AI Translator is a service that enables you to translate text between languages. Follow these steps to provision an Azure AI Translator resource:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com) and sign in with your Microsoft account associated with your Azure subscription.
2. In the search field at the top, search for "Azure AI services" and press Enter.
3. Under the results, select Create under "Translator".
4. Configure the resource with the following settings:
   - Subscription: Your Azure subscription.
   - Resource group: Choose or create a resource group.
   - Region: Choose any available region.
   - Name: Enter a unique name.
   - Pricing tier: Select F0 (free) or S (standard) if F is not available.
   - Responsible AI Notice: Agree.
5. Select Review + create.
6. Wait for deployment to complete, and then go to the deployed resource.
7. View the Keys and Endpoint page. 

### Create an env file to store credentials

- Add a `.env` file with Azure service credentials:
  ```
  TRANSLATOR_KEY=your_translator_key
  TRANSLATOR_REGION=your_translator_region
  ```

## How to Use
Run the script and follow the prompts to input text for translation and select a target language:

```
python3 translate.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained practical experience in using Azure AI services for language translation.
- Developed skills in creating interactive applications using Azure's cognitive services.
- Enhanced understanding of real-world applications of AI in overcoming language barriers.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
