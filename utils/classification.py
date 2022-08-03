from numpy import full
from tensorflow import keras
from imageai.Detection import ObjectDetection
import os


results={
   0:'aeroplane',
   1:'automobile',
   2:'bird',
   3:'cat',
   4:'deer',
   5:'dog',
   6:'frog',
   7:'horse',
   8:'ship',
   9:'truck'
}

def classify_image(base_path, relative_path, model_path):
   from PIL import Image
   import numpy as np
   print(model_path)
   model = keras.models.load_model(model_path)
   full_path = f"{base_path}{relative_path}"
   im=Image.open(full_path)
   im=im.resize((32,32))
   im=np.expand_dims(im,axis=0)
   im=np.array(im)
   pred=np.argmax(model.predict([im])[0])
   return results[pred]



def classify_image_better(base_path, relative_path, model_path):
   detector = ObjectDetection()
   detector.setModelTypeAsRetinaNet()
   detector.setModelPath(model_path=model_path)
   detector.loadModel()
   full_path = f"{base_path}{relative_path}"
   path, ext = os.path.splitext(relative_path)
   output_path = f"{base_path}{path}_output{ext}"
   detector.detectObjectsFromImage(input_image=full_path, output_image_path=output_path)
   return f"{path}_output{ext}"









