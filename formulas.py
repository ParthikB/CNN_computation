import numpy


def layer_properties(info):
    print(info.items())
    for k,v in info.items():
        print(k, v)


# layer_properties({"123":123, "layer":5})

def compute_conv_layer(prev_x, prev_y, filter_channels, filter_size, padding, stride):
    x_dim = ((prev_x + (2*padding) - filter_size)/stride) + 1
    y_dim = ((prev_y + (2*padding) - filter_size)/stride) + 1
    c_dim = filter_channels
    return (x_dim, y_dim, c_dim)


