from xmlrpc.client import ResponseError
from django.db import models # import the Django models namespace

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "input." + extension

# Our main model: Uploaded Image
class UploadedImage(models.Model):
    image = models.ImageField("Uploaded Image", upload_to=scramble_uploaded_filename) # stores the filename of an uploaded image
