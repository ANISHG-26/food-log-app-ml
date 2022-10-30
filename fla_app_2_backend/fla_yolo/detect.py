import torch

class FoodDetection:

    def __init__(self,capture_index,model_name):

        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ",self.device)

    def load_model(self, model_name):
        
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        return model

    def predict_object(self, image):
        self.model.to(self.device)
        results = self.model(image, size=640)
        
        try:
            object_detected = results.pandas().xyxy[0]["name"][0]
            object_detected = object_detected.strip()
        except:
            object_detected = "Unable to detect"
        
        return object_detected