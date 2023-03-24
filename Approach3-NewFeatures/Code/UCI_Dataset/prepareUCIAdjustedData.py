import numpy as np
from reformatUCIDataset import get_adjusted_dataset


def shuffle_data(array):
    perm = np.random.permutation(len(array))

    return array[perm]


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
    print("Getting data...")
    dataset = get_adjusted_dataset()

    # shuffle data
    # print("Shuffling data...")
    # dataset = shuffle_data(dataset)
    print(dataset)

    # strip testing and training data
    length = len(dataset)
    training_data_number = round(length * 0.7)  # currently a 70/30 split testing and training
    length -= training_data_number

    testing_data_number = length
    training_data = dataset[:training_data_number]
    testing_data = dataset[training_data_number:]

    print("Training data:\t\t", training_data_number, "\nTesting data:\t\t", testing_data_number)
    training_features, training_labels = feature_and_labels(training_data)
    testing_features, testing_labels = feature_and_labels(testing_data)

    print("Data preparation done!")

    return training_features, training_labels, testing_features, testing_labels


if __name__ == "__main__":
    prepare_data()
