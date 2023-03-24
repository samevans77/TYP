import numpy as np
from createArrays import create_url_array


def shuffle_data(data):
    np.random.shuffle(data)
    return data


def strip_last_column(data):  # strips the last column (the label) from the remainder of the file (the feature)
    data_label = data[data.size-1:]
    data_feature = data[:data.size-1]
    return data_feature, data_label


def feature_and_labels(data):
    output_features = []
    output_labels = []

    # taking a dataset and converting it to features and labels
    for data_point in data:
        feature, label = strip_last_column(data_point)
        output_features.append(feature)
        output_labels.append(label)

    return np.array(output_features), np.array(output_labels)


def prepare_data():
    # get data
    print("Creating data...")
    url_array = create_url_array()

    # shuffle data
    print("Shuffling data...")
    url_array = shuffle_data(url_array)

    length = len(url_array)

    print("Getting training data...")

    training_data_number = round(length * 0.7)  # doing a 70/30 split for training, testing data.

    length -= training_data_number

    testing_data_number = round(length)

    # getting the training data first
    training_data = url_array[:training_data_number]

    # then the testing data
    testing_data = url_array[training_data_number:training_data_number + testing_data_number]

    print("\nTraining data:\t\t", training_data_number, "\nTesting data:\t\t", testing_data_number)

    print("Splitting features and labels...")

    # split to get feature and label lists.
    training_features, training_labels = feature_and_labels(training_data)
    testing_features, testing_labels = feature_and_labels(testing_data)

    print("Data preparation done!")

    return training_features, training_labels, testing_features, testing_labels


if __name__ == "__main__":
    prepare_data()

