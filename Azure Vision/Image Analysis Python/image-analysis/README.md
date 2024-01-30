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
git clone <repository-url>
cd <project-directory>
pip install azure-cognitiveservices-vision-computervision python-dotenv pillow
```

## Configuration
- Set up Azure Cognitive Services in the Azure portal.
- Create a `.env` file with your Computer Vision service credentials:
  ```
  VISION_KEY=your_vision_key
  VISION_ENDPOINT=your_vision_endpoint
  ```

## How to Use
To run the script:

```
python script_name.py [optional: path_to_image]
```
Replace `script_name.py` with the name of your script, and provide an image path if needed.

## Example Output
The script outputs the analysis of the provided image, including categories, a description, and tags identified by Azure's Computer Vision.

## Learning Outcomes
- Gained experience in using Azure Cognitive Services for advanced image processing.
- Developed skills in integrating cloud AI services with Python applications.
- Enhanced understanding of Computer Vision concepts and their practical applications.

## Acknowledgments
This project was developed as part of the exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).
