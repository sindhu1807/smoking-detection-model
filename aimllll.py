# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:31:03 2024

@author: Dell
"""

import numpy as np
from flask import Flask, render_template, request
import pickle
app=Flask(__name__)
model=pickle.load(open('mrs/mr.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    output=round(prediction[0],2)
    return render_template('index.html', prediction_text='Prediction of smoking is {}'.format(output))

if __name__ == "__main__":
    app.run()
