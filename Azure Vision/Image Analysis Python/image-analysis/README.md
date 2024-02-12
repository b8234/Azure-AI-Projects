# Analyze Images - Computer Vision

## Description
This project is a part of the Microsoft AI MS Learn series and focuses on implementing Azure Cognitive Services' Computer Vision to analyze images. The Python script utilizes the Computer Vision API to extract features like categories, descriptions, and tags from a provided image, demonstrating a key application of cloud-based AI in image processing.

## Objectives
- Utilize Azure Cognitive Services' Computer Vision for image analysis.
- Extract categories, descriptions, and tags from images using Azure AI capabilities.
- Demonstrate practical image processing skills in a cloud environment.

## Technologies Used
- Azure Cognitive Services - Computer Vision.
- Python for scripting and interaction with Azure services.
- Python Imaging Library (PIL) for image handling.

## Setup and Installation
To set up and run this project:

```
git clone https://github.com/b8234/Azure-AI-Projects.git
cd Azure-AI-Projects/Azure\ Vision/Image\ Analysis\ Python/image-analysis
```

Run command to install packages:

```
pip3 install azure-cognitiveservices-vision-computervision msrest python-dotenv Pillow
```

Or install the required dependencies via requirements, run the following command:

```bash
pip3 install -r requirements.txt
```

## Configuration

### Provision an Azure AI Services Resource

If you don’t already have one in your subscription, you’ll need to provision an Azure AI Services resource. Follow these steps:

1. Open the Azure portal at [https://portal.azure.com](https://portal.azure.com) and sign in using the Microsoft account associated with your Azure subscription.

2. In the top search bar, search for "Azure AI services" and select Azure AI Services.

3. Create an Azure AI services multi-service account resource with the following settings:
   - **Subscription:** Your Azure subscription.
   - **Resource group:** Choose or create a resource group. (If you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided).
   - **Region:** Choose from East US, France Central, Korea Central, North Europe, Southeast Asia, West Europe, West US, or East Asia. *Note: Azure AI Vision 4.0 features are currently only available in these regions.*
   - **Name:** Enter a unique name.
   - **Pricing tier:** Standard S0 or Free Tier.
   
4. Select the required checkboxes and create the resource.

5. Wait for deployment to complete, and then view the deployment details.

6. When the resource has been deployed, go to it and view its Keys and Endpoint page. You will need the endpoint and one of the keys from this page in the next procedure.

### Create an .env file to store credentials

- Create a `.env` file with your Computer Vision service credentials:
  ```
  VISION_KEY=your_vision_key
  VISION_ENDPOINT=your_vision_endpoint
  ```

## How to Use
To run the script:

```
python3 image_analysis.py 
```
Replace `image_analysis.py` with the name of your script, and provide an image path if needed.

## Example Output
Example output is in the Output folder.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for advanced image processing.
- Developed skills in integrating cloud AI services with Python applications.
- Enhanced understanding of Computer Vision concepts and their practical applications.

## Acknowledgments
This project is inspired by exercises in the [Microsoft AI MS Learn series](https://learn.microsoft.com/en-us/training/).

## Contact

If you have any questions or feedback, feel free to [open an issue](https://github.com/b8234/Azure-AI-Projects/issues/new). I welcome your input and suggestions to improve this repository further.
