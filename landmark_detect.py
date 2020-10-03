import io
import os

from google.cloud import vision
#from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'


client = vision.ImageAnnotatorClient()

file_name = 'image3.jpg'
image_path = f'./uploads/images/{file_name}'

# 'rb' opens a file for reading in binary format

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

#image = vision.types.Image(content=content)
image = vision.Image(content=content)
response = client.landmark_detection(image=image)
landmark = response.landmark_annotations[0]

#print('Location:')
##for landmark in landmarks:
#print("Location found!")
#print(landmark.description)
#print(landmark.score)
for location in landmark.locations:
    lat_lng = location.lat_lng
#    print('Latitude {}'.format(lat_lng.latitude))
#    print('Longitude {}'.format(lat_lng.longitude))

if response.error.message:
    raise Exception('Could not determin the location of the photo.')

landmark_description = landmark.description
landmark_lat = lat_lng.latitude
landmark_long = lat_lng.longitude