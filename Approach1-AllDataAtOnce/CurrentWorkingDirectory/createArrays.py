import numpy as np
from convertToUnicodeCode import convert_to_unicode as convert

# open both files
with open('SourceFiles/phishingLinks.txt', 'r') as phishingFile:
    phishing_list_of_lines = phishingFile.readlines()

with open('SourceFiles/benignLinks.txt', 'r') as benignFile:
    benign_list_of_lines = benignFile.readlines()

max_length = 0
phishing_length = 0
benign_length = 0

# detecting the largest length of the URLs.
for line in phishing_list_of_lines:
    if len(line) > max_length:
        max_length = len(line)
    phishing_length += 1

for line in benign_list_of_lines:
    if len(line) > max_length:
        max_length = len(line)
    benign_length += 1

print("Total phishing data points:\t", phishing_length, "\nTotal benign data points:\t", benign_length)


def create_url_array():
    output = []

    for line_in in phishing_list_of_lines:
        output.append(convert(line_in, max_length) + [1])  # appending the label on the end (easier shuffling)

    for line_in in benign_list_of_lines:
        output.append(convert(line_in, max_length) + [0])

    return np.array(output)


# Order is important between phishing and benign, since this will be training and testing data.
def create_phishing_array():
    output = []
    for line_in in phishing_list_of_lines:
        output.append(1)

    for line_in in benign_list_of_lines:
        output.append(0)

    return np.array(output)


if __name__ == "__main__":
    # creates the single feature matrix containing the values of all the phishing and benign outputs.
    print(create_url_array())

    # creates the label matrix for this.
    # print(create_phishing_array())

    # FOR NOW, APPENDING THE LABEL ON THE END SO THAT SHUFFLING WILL BE A LOT LESS PAINFUL
