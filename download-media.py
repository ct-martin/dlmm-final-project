import boto3
from botocore import UNSIGNED
from botocore.client import Config
import io
import json
import multiprocessing
import os
from PIL import Image

# S3 client, will get created on init()
client = None

# Disable image size limit
Image.MAX_IMAGE_PIXELS = None

def initialize():
  global client
  client = boto3.client('s3', region_name="us-west-2", config=Config(signature_version=UNSIGNED))

def download_image(media_id):
  if not os.path.isfile(f"media/{media_id}.jpg"):
    img_data = client.get_object(Bucket="smithsonian-open-access", Key=f"media/chsdm/{media_id}.jpg")['Body'].read()
    image = Image.open(io.BytesIO(img_data))
    image.thumbnail((1024,1024))
    image.save(f"media/{media_id}.jpg",'jpeg',quality=80)
    del image
    del img_data

if __name__ == '__main__':
  # Get list of media ids
  media_ids = None
  with open("si-download.json") as file:
    media_ids = set(json.load(file))
  print("Files to download:",len(media_ids))

  # Create Pool
  pool = multiprocessing.Pool(multiprocessing.cpu_count(), initialize)
  
  # Assign jobs
  pool.map(download_image, media_ids)

  # Clean up
  pool.close()
  pool.join()

