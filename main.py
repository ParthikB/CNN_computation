import numpy
from formulas import *

class Layer:
    def __init__(self):
        self.type         = None
        self.nodes        = None
        self.height       = None
        self.width        = None
        self.channels     = None
        self.padding      = None
        self.stride       = None
        self.filter_size  = None
        self.filter_count = None


if __name__ == '__main__':

    input_img_shape = input('Enter Input Image Shape {x, y} : ')
    split = input_img_shape.split(',')

    input_img_shape  = (int(split[0]), int(split[-1]))
    input_x, input_y = input_img_shape
    number_of_layers = int(input('Enter number of Layers : '))

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

        print(layers['layer_' + str(layer_num)].__dict__)
        print(layers)
        print()


    for layer_name, layer in layers.items():
        if layer.type != 'linear':
            dims = compute_conv_layer(prev_x          = input_x, 
                                    prev_y            = input_x, 
                                    filter_channels   = layer.filter_count, 
                                    filter_size       = layer.filter_size, 
                                    padding           = layer.padding, 
                                    stride            = layer.stride)
            print(dims)
        else:
            print('Linear Layer!')
        