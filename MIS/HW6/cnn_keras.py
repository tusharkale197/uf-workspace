from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
import matplotlib.pylab as plt
import os
import time
def cnn_using_keras(training_curves, kern_size=5, conv_1_activation="relu", conv_2_activation="relu", opt=keras.optimizers.Adam(), one_each_no_max=False, config = "default"):
    """
    Function to build CNN layers based on the input parameters to the function and train and test 
    """
    try:
        batch_size = 128
        num_classes = 10
        epochs = 10

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
        y_train = keras.utils.to_categorical(y_train, num_classes)
        y_test = keras.utils.to_categorical(y_test, num_classes)

        model = Sequential()
        model.add(Conv2D(32, kernel_size=(kern_size, kern_size), strides=(1, 1),
                         activation=conv_1_activation,
                         input_shape=input_shape))
        if not one_each_no_max:
            model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
            model.add(Conv2D(64, (kern_size, kern_size), activation=conv_2_activation))
            model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        if not one_each_no_max:
            model.add(Dense(1000, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=opt,
                      metrics=['accuracy'])


        class AccuracyHistory(keras.callbacks.Callback):
            def on_train_begin(self, logs={}):
                self.acc = []
                self.loss = []
                self.times = []

            def on_epoch_begin(self, batch, logs={}):
                self.epoch_time_start = time.time()

            def on_epoch_end(self, batch, logs={}):
                self.times.append(time.time() - self.epoch_time_start)
                self.acc.append(logs.get('acc'))
                self.loss.append(logs.get('loss'))


        history = AccuracyHistory()

        model.fit(x_train, y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  verbose=1,
                  validation_data=(x_test, y_test),
                  callbacks=[history])
        score = model.evaluate(x_test, y_test, verbose=0)
        
        # Writing the final test and train scores to a text file
        file = open("cnn_results.txt","a")
        file.write(config)
        file.write("\n")
        file.write("Test loss: %s \n" %score[0])
        file.write("Test accuracy: %s \n" %score[1])
        file.write("Train loss: %s \n" % history.loss[-1])
        file.write("Train accuracy: %s \n" %history.acc[-1])
        file.write("****************************** \n")
        file.close()
        
        training_curves["accuracy_curve"][config] = history.acc
        training_curves["loss_curve"][config] = history.loss
        training_curves["time_curve"][config] = history.times
        
        save_location="/Users/tusharkale/Desktop"
        acc_plots_loc = '%s/accuracy' %save_location
        plt.plot(range(1, 11), history.acc)
        average_time = int(sum(history.times)/ len(history.times))
        plt.title("%s Avg time:%s secs"%(config, average_time))

        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.savefig("%s/%s.png" %(acc_plots_loc, config))
        plt.clf()

        acc_plots_loc = '%s/loss' %save_location
        plt.plot(range(1, 11), history.loss)
        plt.title("%s"%config)

        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.savefig("%s/%s.png" %(acc_plots_loc, config))
        plt.clf()
        return training_curves
        
    except Exception as e:
        raise e


def compare_settings(kernal_size, optimizer, authors_case=False, optmizer_name="Adam"):
    """
        Function call cnn_using_keras for different combinations
    """
    # file = open("cnn_results.txt","w")
    training_curves = dict()
    training_curves["accuracy_curve"] = dict()
    training_curves["loss_curve"] = dict()
    training_curves["time_curve"] = dict()

    # Different kernal size
    config_text = "Kernal size %s and %s optimizer -> Relu -> Relu" % (kernal_size,  optmizer_name)
    if authors_case:
        config_text= "Adventures in Machine Learning original config"
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      config=config_text,
                                      opt=optimizer)
    time.sleep(20)
    # Different Non linearities tanh followed by RELU
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      conv_1_activation="tanh", 
                                      config="Kernal size %s and %s optimizer->tanh->Relu" % (kernal_size,  optmizer_name),
                                      opt=optimizer)
    time.sleep(20)
    # Different Non linearities RELU followed by tanh
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      conv_2_activation="tanh", 
                                      config="Kernal size %s and %s optimizer->Relu->tanh" % (kernal_size,  optmizer_name),
                                      opt=optimizer)
    time.sleep(20)
    # Different Non linearities only tanh 
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      conv_1_activation="tanh", 
                                      conv_2_activation="tanh", 
                                      config="Kernal size %s and %s optimizer->tanh->tanh" % (kernal_size,  optmizer_name),
                                      opt=optimizer)
    time.sleep(20)
    # One convolution layer and one fully connected layer and no max pooling
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      one_each_no_max=True, 
                                      conv_1_activation="tanh", 
                                      config="Kernal size %s and %s optimizer->tanh->no max pool" % (kernal_size,  optmizer_name),
                                      opt=optimizer)
    
    # One convolution layer and one fully connected layer and no max pooling
    training_curves = cnn_using_keras(training_curves, 
                                      kern_size=kernal_size,
                                      one_each_no_max=True, 
                                      config="Kernal size %s and %s optimizer->relu->no max pool" % (kernal_size,  optmizer_name),
                                      opt=optimizer)
    time.sleep(20)
   
    return training_curves


def test_all_settings():
    """
        Function to call the compare_settings with different combinations of parameters for CNN layers
    """
    try:
        data_kern_5_adam = dict()
        data_kern_5_sgd = dict()
        data_kern_9_adam = dict()
        data_kern_9_sgd = dict()
        data_kern_3_adam = dict()
        data_kern_3_sgd = dict()

        # Kernal size 5 and Adam optmizers with different combinations of non linearities
        data_kern_5_adam = compare_settings(kernal_size=5, optimizer=keras.optimizers.Adam(), authors_case= True, optmizer_name="Adam" )
        
        # Kernal size 5 and SGD optmizers with different combinations of non linearities
        data_kern_5_sgd = compare_settings(kernal_size=5, optimizer=keras.optimizers.SGD(), authors_case= False, optmizer_name="SGD" )

        # Kernal size 9 and Adam optmizers with different combinations of non linearities
        data_kern_9_adam = compare_settings(kernal_size=9, optimizer=keras.optimizers.Adam(), authors_case= False, optmizer_name="Adam" )
        
        # Kernal size 9 and SGD optmizers with different combinations of non linearities
        data_kern_9_sgd = compare_settings(kernal_size=9, optimizer=keras.optimizers.SGD(), authors_case= False, optmizer_name="SGD" )
        
        # Kernal size 3 and Adam optmizers with different combinations of non linearities
        data_kern_3_adam = compare_settings(kernal_size=3, optimizer=keras.optimizers.Adam(), authors_case=False, optmizer_name="Adam")
        
        # Kernal size 3 and SGD optmizers with different combinations of non linearities
        data_kern_3_sgd = compare_settings(kernal_size=3, optimizer=keras.optimizers.SGD(), authors_case=False, optmizer_name="SGD")
        return data_kern_5_adam, data_kern_5_sgd, data_kern_9_adam, data_kern_9_sgd, data_kern_3_adam, data_kern_3_sgd
    
    except Exception as exc:
        raise exc


def plot_and_save_curves(data, save_location):
    """
    Function to plot and save all the graphs for the accuracy, loss and time data for all the possible case
    PLEASE NOTE: This function is NOT used anywhere since graph plotting and saving is done explicitly at the end of each case
    """
    try:
        acc_plots_loc = '%s/accuracy' % save_location
        accuracy_data = data["accuracy_curve"]
        time_data = data["time_curve"]
        loss_data = data["loss_curve"]
        for config in accuracy_data:
            plt.plot(range(1, 11), accuracy_data[config])
            average_time = int(sum(time_data[config])/len(time_data[config]))
            plt.title("%s Avg time:%s secs" % (config, average_time))

            plt.xlabel('Epochs')
            plt.ylabel('Accuracy')
            plt.savefig("%s/%s.png" % (acc_plots_loc, config))
            plt.clf()

        acc_plots_loc = '%s/loss' % save_location
        for config in loss_data:
            plt.plot(range(1, 11), loss_data[config])
            plt.title("%s" % config)

            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.savefig("%s/%s.png" % (acc_plots_loc, config))
            plt.clf()
    except Exception as exc:
        raise exc

if __name__ == '__main__':
    test_all_settings()