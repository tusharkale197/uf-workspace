"""
Math for Intelligent Systems Homework 4
Problem statement:
2. Multi-class Linear Classifier
•   Download the Iris dataset available at the UCI Machine Learning repository in the platform of your choice.
•   Execute a homegrown multi-class least-squares classifier on the Iris dataset after separating it into training and test set patterns.
•   Document the training and testing mis-classification errors and separate out each class errors using a confusion matrix (3 × 3 with diagonal values being true positives).
•   Document the settings of the free parameters (if any). Give a high level summary of your findings based on your interpretation of the results.
•   The ratios attempted for training and testing should be 12% training/88% testing, 30% train- ing/70% testing and 50% training/50% testing
    (and these percentages should be class spe- cific as much as possible). There is no need to perform cross-validation.
•   Include the source code and printouts in your submitted homework. Add a link to the pdf if you wish.
"""

import numpy as np
import math


class MulticlassClassifier:

    @staticmethod
    def read_and_partition_data(classes_dict, data_file_path, training=50):
        """
        This function takes the data file and partitions into test and training according to the given percentages

        :param classes_dict: (dict)
        :param data_file_path: (str) Location of the datat file
        :param training:(int) Size of the training set as a percentage of total data
        :return: Returns X matrix containing all the feature vectors Y matrix with corresponding classification and the rest of the test data
        """
        try:
            f = open(data_file_path)
            contents = f.readlines()

            # Dictionary that stores the x vlaues of different classes
            classes_x_values = dict(classes_dict)

            # Initialising the classes_x_values dict to empty list
            for key in classes_x_values:
                classes_x_values[key] = list()
            num_feats = 0
            for data in contents:
                # this accounts for empty lines in the data file

                if data.strip():
                    data_split = data.split(",")
                    x_values = [float(x) for x in data_split[:-1]]
                    num_feats = len(x_values)
                    class_value = data_split[-1].rstrip()
                    classes_x_values[class_value].append(x_values)

            training_data = list()
            test_data = list()
            train_yt_values = list()
            test_yt_values = list()
            for key in classes_x_values:
                data_temp = classes_x_values[key]
                data_len = len(data_temp)
                training_len = math.floor((training/100)*data_len)
                training_data.extend(data_temp[:training_len])
                train_yt_values.extend([classes_dict[key]] * training_len)
                test_data.extend(data_temp[training_len:])
                test_yt_values.extend([key] * (data_len-training_len))
            return training_data, test_data, train_yt_values, num_feats, test_yt_values
        except Exception as exc:
            raise exc

    @staticmethod
    def compute_weight_matrix(feature_vectors, feature_vects_transpose, class_vectors, lambda_value, num_features):
        """
            Returns the weight matrix for the multi class classifier
        :param feature_vectors:
        :param feature_vects_transpose
        :param class_vectors:
        :param lambda_value:
        :param num_features
        :return:
        """
        try:
            first_component = np.matmul(feature_vectors, feature_vects_transpose) + lambda_value * np.identity(num_features)
            inv_first_comp = np.linalg.inv(first_component)
            second_component = np.matmul(feature_vectors, class_vectors)
            w_matrix = np.matmul(inv_first_comp, second_component)
            return w_matrix
        except Exception as exc:
            raise exc

    def classify_test_data_bulk(self, w_matrix, test_data, test_ytrans_values):
        """

        :param w_matrix:
        :param test_data:
        :param test_ytrans_values:
        :return:
        """
        try:
            for i in range(0, len(test_data)):
                class_name = self.classify_test_data_single(w_matrix, test_data[i])
                if class_name == test_ytrans_values[i]:
                    print("Success")
                else:
                    print("Check it tomorrow")

        except Exception as exc:
            raise exc

    @staticmethod
    def classify_test_data_single(w_matrix, test_data):
        """

        :param w_matrix:
        :param test_data:
        :return:
        """
        try:
            w_1_transpose = w_matrix[:, [0]].transpose()
            w_2_transpose = w_matrix[:, [1]].transpose()
            w_3_transpose = w_matrix[:, [2]].transpose()

            w1_trans_x = np.matmul(w_1_transpose, test_data)
            w2_trans_x = np.matmul(w_2_transpose, test_data)
            w3_trans_x = np.matmul(w_3_transpose, test_data)

            if w1_trans_x > w2_trans_x:
                if w1_trans_x > w3_trans_x:
                    return "Iris-setosa"
                else:
                    return "Iris-versicolor"
            else:
                if w2_trans_x > w3_trans_x:
                    return "Iris-versicolor"
                else:
                    return "Iris-virginica"

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    print("All the HW 4 classifier code goes here")
    m = MulticlassClassifier()
    # Dictionary with different classes and their discrminating vector
    class_dict = dict()
    class_dict["Iris-setosa"] = [1, 0, 0]
    class_dict["Iris-versicolor"] = [0, 1, 0]
    class_dict["Iris-virginica"] = [0, 0, 1]

    # This function reads the data from the data file and segregates it into training and test
    training_xt_values, testing_data, training_yt_values, feature_count, testing_yt_values = m.read_and_partition_data(class_dict, "iris.data", 50)

    training_xt_values = np.asarray(training_xt_values)
    training_x_values = training_xt_values.transpose()
    training_yt_values = np.asarray(training_yt_values)
    lamb_value = 0.0001

    # Computing the weight matrix
    weight_matrix = m.compute_weight_matrix(training_x_values, training_xt_values, training_yt_values, lamb_value, feature_count)
    print(testing_data[0])
    print(testing_data)
    # Classify
    m.classify_test_data_bulk(weight_matrix, testing_data, testing_yt_values)
