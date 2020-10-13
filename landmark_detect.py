import io
import os
import wikipedia_summary

from google.cloud import vision
#from google.cloud.vision import types

def location(file_name):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'


    client = vision.ImageAnnotatorClient()

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

    #os.remove({file_name})

    return {'description':landmark.description, 'lat': lat_lng.latitude, 'long': lat_lng.longitude, 'summary': wikipedia_summary.summary(landmark.description)}