from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import os
from PIL import Image
import sys

'''
Authenticate
Authenticates your credentials and creates a client.
'''
load_dotenv()

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
END - Authenticate
'''

def main():
    try:
        # Get Configuration Settings
        image_file = 'images/person.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Analyze image
        AnalyzeImage(image_file, computervision_client)

    except Exception as ex:
        print(ex)

def AnalyzeImage(image_file, cv_client):
    print('\nAnalyzing', image_file)

    # Specify features to be retrieved
    features = [VisualFeatureTypes.categories, VisualFeatureTypes.description, VisualFeatureTypes.tags]

    # Open and read the local image file
    with open(image_file, 'rb') as image_stream:
        results = cv_client.analyze_image_in_stream(image_stream, visual_features=features)

    # Print image analysis results
    if results.categories:
        print("Categories:")
        for category in results.categories:
            print(f"- {category.name} (confidence: {category.score})")

    if results.description:
        print("\nDescription:")
        print(f"- {results.description.captions[0].text} (confidence: {results.description.captions[0].confidence})")

    if results.tags:
        print("\nTags:")
        for tag in results.tags:
            print(f"- {tag.name} (confidence: {tag.confidence})")

if __name__ == "__main__":
    main()