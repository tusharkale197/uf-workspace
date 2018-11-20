from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
import random
from keras import backend as kb
import matplotlib.pylab as plt


def layer_images():
    num_classes = 10

    # input image dimensions
    img_x, img_y = 28, 28

    # load the MNIST data set, which already splits into train and test sets for us
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # reshape the data into a 4D tensor - (sample_number, x_img_size, y_img_size, num_channels)
    # because the MNIST is greyscale, we only have a single channel - RGB colour images would have 3
    x_train = x_train.reshape(x_train.shape[0], img_x, img_y, 1)
    x_test = x_test.reshape(x_test.shape[0], img_x, img_y, 1)
    input_shape = (img_x, img_y, 1)

    # convert the data to the right type
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices - this is for use in the
    # categorical_crossentropy loss below

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                     activation='relu',
                     input_shape =input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    # picking a random image from the mnist training data

    random_index = random.randint(1, 60000)

    image = x_train[random_index]
    plt.imshow(image[:, :, 0], cmap='gray')
    plt.show()
    image = image.reshape(1, img_x, img_y, 1)

    inp = model.input                                           # input placeholder
    outputs = [layer.output for layer in model.layers]          # all layer outputs
    functor = kb.function([inp, kb.learning_phase()], outputs)
    layer_outs = functor([image, 1.])
    count_layer = 0
    for layer_out in layer_outs:
        if count_layer > 3:
            break
        count_layer = count_layer + 1

        layer_1 = layer_out[0]
        plot_images(layer_1, layer_1.shape[2])


def plot_images(layer_out, num_channels):
    try:
        image_x, image_y = get_image_dim(num_channels)
        f, axarr = plt.subplots(image_x, image_y)
        image_index = 0
        for i in range(0, image_x):
            for j in range(0, image_y):
                axarr[i, j].imshow(layer_out[:, :, image_index], cmap='gray')
                image_index = image_index + 1
        plt.show()

    except Exception as exc:
        raise exc


def get_image_dim(num_channels):
    try:
        if num_channels == 32:
            return 4, 8
        if num_channels == 64:
            return 8, 8
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    layer_images()
