from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load('reg_model.pkl')
pca_model = load('pca.pkl')

class_names = ['DEATH', 'ALIVE']


def my_prediction(array):
    input = np.array(array)
    inputT = input.reshape(1,-1)
    in_tr = pca_model.transform(inputT);
    prediction = my_model.predict(in_tr)
    name = class_names[prediction[0]]
    name_str = json.dumps(name)
    return name_str

#print(my_prediction([50, 0, 100, 0, 30, 0, 204000, 1.4, 130, 0, 1, 10]))
#http://localhost:8080/engr-222/predict/50, 0, 100, 0, 30, 0, 204000, 1.4, 130, 0, 1, 10

