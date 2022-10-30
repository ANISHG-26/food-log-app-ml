from .detect import FoodDetection
from django.core.files.storage import default_storage
from PIL import Image
from rest_framework.decorators import api_view
from django.http import JsonResponse
import os

@api_view(["GET"])
def predicted_result(request):
    predicted_label = None
    path = 'image/input.jpg'
    image = Image.open(path).resize((360,360))
    #image.save('image/resized.jpg')     

    # get predicted label with previously implemented PyTorch function
    try:
        detector = FoodDetection(capture_index=1, model_name='weights/best.pt')
        predicted_label = detector.predict_object(image)
       
    except RuntimeError as re:
        print(re)

    if predicted_label == 'apple':
        response_data = { 'predictedLabel': predicted_label, 'details': 'An Apple (147g) contains 88 calories' }
    
    elif predicted_label == 'banana':
        response_data = { 'predictedLabel': predicted_label, 'details': 'A Banana (47g) contains 55 calories' }
    
    elif predicted_label == 'croissant':
        response_data = { 'predictedLabel': predicted_label, 'details': 'A Butter Croissant (60g) contains 232 calories' }
    
    elif predicted_label == 'donut':
        response_data = { 'predictedLabel': predicted_label, 'details': 'A Plain Donut (60g) contains 220 calories' }

    elif predicted_label == 'sandwich':
        response_data = { 'predictedLabel': predicted_label, 'details': 'A Vegetable Sandwich (167g) contains 225 calories' }
    
    else:
        response_data = { 'predictedLabel': predicted_label, 'details': 'Please try again' }
    
    if os.path.exists(path):
        os.remove(path)
    
    return JsonResponse(response_data)
    
