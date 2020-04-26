#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import json
import base64
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array, load_img


app = Flask(__name__)

model_file = './model/model.h5'
global model
model = keras.models.load_model(model_file)


@app.route('/')
def index():
    response = {}
    return render_template("index.html", **response) 

@app.route('/predict/', methods=['Get', 'POST'])
def preditc():
    parseImage(request.get_data())
    img = img_to_array(load_img('output.png', target_size=(28, 28), color_mode="grayscale")) / 255.
    img = np.expand_dims(img, axis=0)
    code = model.predict_classes(img)[0]
    response = {}
    response['code'] = int(code)
    print(response)
    return jsonify(response)


def parseImage(imgData):
    imgStr = re.search(b'base64,(.*)', imgData).group(1)
    with open('./output.png', 'wb') as output:
        output.write(base64.decodebytes(imgStr))
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10170, debug=False)