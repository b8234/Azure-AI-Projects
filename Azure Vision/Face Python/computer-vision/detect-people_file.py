from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import os
from PIL import Image

# Load configuration from .env file
load_dotenv()

# Authenticate
subscription_key = os.getenv("VISION_KEY")
endpoint = os.getenv("VISION_ENDPOINT")

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Quickstart variables
# Set the path to the local folder where your images are stored
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
local_image_path = os.path.join(images_folder, "people.jpg") # Replace with your local image file name

# Tag an Image - local
print("===== Tag an image - local =====")
# Open local image file
with open(local_image_path, "rb") as local_image:
    # Call API with local image
    tags_result_local = computervision_client.tag_image_in_stream(local_image)

# Print results with confidence score
print("Tags in the local image: ")
if len(tags_result_local.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()

print("End of Computer Vision quickstart.")
