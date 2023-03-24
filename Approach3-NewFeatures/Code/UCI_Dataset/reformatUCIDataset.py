import csv
import numpy as np

# Takes the UCI csv dataset and transforms it into input data for the model.
# We only want features 1, 2, 3, 4, 5, 6, 7, and label


def get_adjusted_dataset():
    line_count = 0
    dataset = []
    with open("../../Data/uci-ml-phishing-dataset.csv", mode="r") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            line_data = []
            line_count += 1
            if line_count != 1:
                for i in range(1, 8):
                    line_data.append(int(line[i]))  # features 1-7 (inclusive)
                line_data.append(int(line[31]))  # label
                dataset.append(line_data)

    return np.array(dataset)


if __name__ == "__main__":
    print(get_adjusted_dataset())
