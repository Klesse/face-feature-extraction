"""
CREATE TABLE face_features(id SERIAL PRIMARY KEY, 
                           name VARCHAR(255),
                           access TIMESTAMP,
                           feature JSON);
"""
import tensorflow as tf
from tensorflow import keras
from keras.applications import VGG16
from keras.models import Model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import psycopg2
import numpy as np
import json
import datetime


class FaceRecognition:
    def __init__(self):
        self.user, self.password = self._read_credentials()

        self.model = VGG16(weights='imagenet', include_top=False)
        self.conn = psycopg2.connect(database = "features", 
                        user = self.user, 
                        host= 'localhost',
                        password = self.password,
                        port = 5432)
        self.cur = self.conn.cursor()
    
    def _read_credentials(self):
        with open('access.txt','r') as f:
            lines = f.readlines()

        return str(lines[0].replace('\n','')), str(lines[1])

    def _extract_features(self, image_path):
        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        features = self.model.predict(img_array)
        return features.flatten()

    def data_to_db(self, image_path):
        features_np = self._extract_features(image_path)
        features_json = json.dumps(features_np.tolist())

        access_time = datetime.datetime.now()

        sql_insert = "INSERT INTO face_features(name, access, feature) VALUES (%s, %s, %s);"
        self.cur.execute(sql_insert, ('Tom Hanks', access_time ,features_json)) # Name to a variable
        self.conn.commit()

    def closest_feature(self, target):
        pass

