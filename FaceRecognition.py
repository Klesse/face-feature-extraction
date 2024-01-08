from tensorflow import keras
from keras.applications import VGG16
from keras.models import Model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np



class FaceRecognition:
    def __init__(self):
        self.model = VGG16(weights='imagenet', include_top=False)

    def extract_features(self, image_path):
        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        features = self.model.predict(img_array)
        return features.flatten()
