import os
import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# set GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of google service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/tg415h/Downloads/google_account_service_key.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('/Users/tg415h/Downloads/dog.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)