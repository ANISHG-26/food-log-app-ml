import torch
from PIL import Image
import pandas

class FoodDetection:

    def __init__(self,capture_index,model_name):

        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ",self.device)

    def get_image(self):
        dim = (680,680)
        
        image = Image.open('../image/input.jpeg')
      
        return image

    def load_model(self, model_name):
        
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        return model

    def predict_object(self, image):
        self.model.to(self.device)
        results = self.model(image, size=640)
        object_detected = results.pandas().xyxy[0]["name"][0]
        object_detected = object_detected.strip()
        print(object_detected)

detector = FoodDetection(capture_index=1, model_name='../weights/best.pt')
detector.predict_object(detector.get_image())
    
