import numpy as np
from createArrays import create_subdomain_array, create_second_level_array, create_top_level_array, \
    create_subdirectory_array, create_additional_feature_array


def shuffle_data(array1, array2, array3, array4, array5):
    perm = np.random.permutation(len(array3))  # assuming that all arrays are the same size (they are in this case)

    return array1[perm], array2[perm], array3[perm], array4[perm], array5[perm]


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
    subdomain_array = create_subdomain_array()
    second_level_array = create_second_level_array()
    top_level_array = create_top_level_array()
    subdirectory_array = create_subdirectory_array()
    additional_feature_array = create_additional_feature_array()

    # shuffle data
    print("Shuffling data...")
    subdomain, second_level, top_level, subdirectory, additional = shuffle_data(subdomain_array, second_level_array, top_level_array
                                                                    , subdirectory_array, additional_feature_array)

    length = len(subdomain)

    print("Getting training data...")
    training_data_number = round(length * 0.7)  # doing a 70/30 split for training, testing data.

    length -= training_data_number

    testing_data_number = round(length)

    length -= testing_data_number

    # getting the training data first
    training_data_subdomain = subdomain[:training_data_number]
    training_data_second_level = second_level[:training_data_number]
    training_data_top_level = top_level[:training_data_number]
    training_data_subdirectory = subdirectory[:training_data_number]
    training_data_additional = additional[:training_data_number]

    # then the testing data
    testing_data_subdomain = subdomain[training_data_number:training_data_number + testing_data_number]
    testing_data_second_level = second_level[training_data_number:training_data_number + testing_data_number]
    testing_data_top_level = top_level[training_data_number:training_data_number + testing_data_number]
    testing_data_subdirectory = subdirectory[training_data_number:training_data_number + testing_data_number]
    testing_data_additional = additional[training_data_number:training_data_number + testing_data_number]

    print("\nTraining data:\t\t", training_data_number, "\nTesting data:\t\t", testing_data_number)

    print("Splitting features and labels...")

    # split to get feature and label lists.
    # training
    training_subdomain_features, training_subdomain_labels = feature_and_labels(training_data_subdomain)
    training_second_level_features, training_second_level_labels = feature_and_labels(training_data_second_level)
    training_top_level_features, training_top_level_labels = feature_and_labels(training_data_top_level)
    training_subdirectory_features, training_subdirectory_labels = feature_and_labels(training_data_subdirectory)
    training_additional_features, training_additional_labels = feature_and_labels(training_data_additional)

    # testing
    testing_subdomain_features, testing_subdomain_labels = feature_and_labels(testing_data_subdomain)
    testing_second_level_features, testing_second_level_labels = feature_and_labels(testing_data_second_level)
    testing_top_level_features, testing_top_level_labels = feature_and_labels(testing_data_top_level)
    testing_subdirectory_features, testing_subdirectory_labels = feature_and_labels(testing_data_subdirectory)
    testing_additional_features, testing_additional_labels = feature_and_labels(testing_data_additional)

    print("Data preparation done!")

    return training_subdomain_features, training_subdomain_labels, training_second_level_features, \
        training_second_level_labels, training_top_level_features, training_top_level_labels, \
        training_subdirectory_features, training_subdirectory_labels, testing_subdomain_features, \
        testing_subdomain_labels, testing_second_level_features, testing_second_level_labels,\
        testing_top_level_features, testing_top_level_labels, \
        testing_subdirectory_features, testing_subdirectory_labels, training_additional_features, \
        training_additional_labels, testing_additional_features, testing_additional_labels


if __name__ == "__main__":
    prepare_data()

