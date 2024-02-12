# Azure Cognitive Services Computer Vision OCR Projects

## Description
These projects are a part of the Microsoft AI MS Learn series and contain two Python scripts demonstrating the use of Azure Cognitive Services Computer Vision for Optical Character Recognition (OCR). The first script performs OCR on a local PDF file, extracting and printing text. The second script does OCR on a remote image, again extracting and printing the text. 

## Objectives
- Implement Azure Cognitive Services Computer Vision for OCR on both local and remote images.
- Extract text from images and present it in a readable format.
- Showcase Azure AI's OCR capabilities in different scenarios.

## Technologies Used
- Azure Cognitive Services Computer Vision.
- Python for scripting and handling image files.
- PIL (Python Imaging Library) for local image processing.

## Setup and Installation
To set up and run these projects:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Optical\ Character\ Recognition\ Python/read-text
```

Run command to install packages:

```bash
pip3 install azure-cognitiveservices-vision-computervision msrest python-dotenv Pillow
```

Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

1. **Sign in to the Azure Portal**:
   - Open a web browser and navigate to [https://portal.azure.com](https://portal.azure.com).
   - Sign in using the Microsoft account associated with your Azure subscription.

2. **Create Azure AI Services Resource**:
   - In the top search bar of the Azure portal, search for "Azure AI services" and select **Azure AI Services** from the suggestions.
   - Click on the **Create** button to begin creating a new Azure AI Services resource.
   - Provide the following details for the resource:
     - **Subscription:** Select your Azure subscription.
     - **Resource group:** Choose an existing resource group or create a new one. (Note: If you have restricted permissions, you may need to use a provided resource group.)
     - **Region:** Choose one of the supported regions (East US, France Central, Korea Central, North Europe, Southeast Asia, West Europe, West US, or East Asia).
     - **Name:** Enter a unique name for your Azure AI Services resource.
     - **Pricing tier:** Select **Standard S0**.
   - Once all details are provided, review the configuration and click on the **Review + create** button.

3. **Deployment and Validation**:
   - Review the summary of your resource configuration, then click **Create** to deploy the resource.
   - Monitor the deployment progress in the Azure portal. Wait for the deployment to complete.
   - After deployment, navigate to the resource you created to view its details.

4. **Retrieve Keys and Endpoint**:
   - In the Azure AI Services resource, locate and navigate to the **Keys and Endpoint** page.
   - Note down the endpoint URL and one of the access keys listed on this page. You'll need these for configuring your applications to access the AI services.

### Create an .env file to store credentials

- Create a `.env` file with your Azure service details:
  ```
  VISION_KEY=your_vision_key
  VISION_ENDPOINT=your_vision_endpoint
  ```

## How to Use
- For local OCR: Place your local image file in the specified directory and run the first script.
- For remote OCR: Run the second script which processes a specified remote image URL.

```
python3 quickstart-file.py
```
```
python3 quickstart-file2.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for OCR tasks.
- Developed skills in processing both local and remote images for text extraction.
- Enhanced understanding of integrating Azure AI services with Python for OCR applications.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
