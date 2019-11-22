from flask import Flask, render_template, request
import numpy as np
import joblib
import os

from main import Layer


# TEMPLATE_DIR = os.path.abspath('../endToend/templates')
# STATIC_DIR = os.path.abspath('../endToend/static')

# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__)


# Defining the Home page
@app.route('/')
def home():
    return render_template('index.html')

# Defining the Prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # try:
        # Taking the inputs and saving them to a variable
        input_img_shape = request.form['input_image_shape']
        split = input_img_shape.split(',')

        input_img_shape  = (int(split[0]), int(split[1]), int(split[-1]))
        input_x, input_y, input_c = input_img_shape
        number_of_layers = float(request.form['number_of_layers'])
        
        layers = {}
        for layer_num in range(number_of_layers):
            layer_num += 1
            
            layers['layer_' + str(layer_num)] = Layer()

            layers['layer_' + str(layer_num)].type = (input(f"Layer_{layer_num} Type (conv/pool/linear) : ")).lower()
            if layers['layer_' + str(layer_num)].type == 'linear':
                layers['layer_' + str(layer_num)].nodes = int(input("Nodes : "))
            else:
                layers['layer_' + str(layer_num)].padding = int(input('Padding : '))
                layers['layer_' + str(layer_num)].stride = int(input('Stride : '))
                layers['layer_' + str(layer_num)].filter_count = int(input('Number of Filters : '))
                layers['layer_' + str(layer_num)].filter_size = int(input('Filter size : '))

            # print(layers['layer_' + str(layer_num)].__dict__)
            # print(layers)

        

        # except:
        #     return 'Invalid Values entered!'

    return render_template('predict.html', dims = 'Enter the output here..')


if __name__ == '__main__':
    app.run(debug=True)