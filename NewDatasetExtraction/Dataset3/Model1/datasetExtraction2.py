import csv
import string


# 0 means legit, 1 means phishing
def format_string(input_string):
    special_characters = list(string.punctuation)

    # take any given string, format it (removing https, www.)
    if input_string.startswith("'"):
        input_string = input_string[1:]  # removes the ' which some parts of the dataset includes.

    if input_string.endswith("'"):
        input_string = input_string[:-1]

    if input_string.startswith("www."):
        input_string = input_string[4:]  # removes the www.

    # next, remove special characters.
    new_string = ""
    for character in input_string:
        if character not in special_characters:
            new_string += character

    output_string = new_string

    return output_string


def generate_files(approach):
    with open('../dataset_phishing.csv', mode='r') as file:
        list_of_lines = csv.reader(file)

        benign_list = []
        phishing_list = []
        index = 0

        for line in list_of_lines:
            index += 1

            if index == 1:
                # do nothing
                print("")
            else:

                url = line[0]
                label = line[88]

                url = url.split('://')[1]
                print(index, url, label)

                # approach one wants a benignlinks.txt file and a phishinglinks.txt file.
                if approach == 1:
                    if label == "legitimate":
                        benign_list.append(format_string(url) + "\n")
                    elif label == "phishing":
                        phishing_list.append(format_string(url) + "\n")

        print(benign_list)
        print(phishing_list)

        if approach == 1:
            with open('phishingLinks.txt', 'w') as file2:
                string_to_write = ''.join(phishing_list)
                file2.write(string_to_write)

            with open('benignLinks.txt', 'w') as file3:
                string_to_write2 = ''.join(benign_list)
                file3.write(string_to_write2)


if __name__ == "__main__":
    generate_files(1)
