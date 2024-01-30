# Azure Computer Vision Image Tagging Projects

## Description
These projects are a part of the Microsoft AI MS Learn series. They use Azure Cognitive Services Computer Vision. The first script tags elements in a local image, while the second script performs similar tagging on a remote image. These projects demonstrate the application of Azure AI in analyzing and categorizing visual content from different sources.

## Objectives
- Implement Azure Cognitive Services Computer Vision for both local and remote image analysis.
- Utilize the Computer Vision API to identify and categorize elements within images.
- Showcase the versatility of Azure AI in interpreting visual data from various sources.

## Technologies Used
- Azure Cognitive Services Computer Vision for image analysis.
- Python for scripting and Azure service integration.
- PIL (Python Imaging Library) for handling local image files.

## Setup and Installation
To set up and run these projects:

```
git clone <repository-url>
cd <project-directory>
pip install azure-cognitiveservices-vision-computervision Pillow
```

## Configuration
- Set up Azure Computer Vision resources in Azure.
- Create a `.env` file with your Azure service credentials:
  ```
  VISION_KEY=your_vision_key
  VISION_ENDPOINT=your_vision_endpoint
  ```

## How to Use
- For local image tagging, run the first script with a local image file.
- For remote image tagging, run the second script which accesses an image via a URL.

```
python local_image_tagging_script.py
python remote_image_tagging_script.py
```

## Example Output
Example output is in the Example Output folder.

## Learning Outcomes
- Gained experience in using Azure AI services for analyzing both local and remote images.
- Developed skills in creating Python applications that leverage Azure Cognitive Services for computer vision tasks.
- Enhanced understanding of the practical applications of AI in image processing and analysis.

## Acknowledgments
These projects were inspired by exercises in the [Microsoft AI MS Learn series](link_to_the_relevant_MS_Learn_module).

