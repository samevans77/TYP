# https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset
import csv
import string


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


# opening the CSV file
def generate_files():
    with open('SourceFiles/urlset.csv', mode='r') as file:
        # reading the CSV file
        csv_file = csv.reader(file)
        line_no = 2
        out_phishing = 0
        out_legit = 0
        phishing_list = []
        benign_list = []
    # displaying the website URLs
        for line in csv_file:
            print("Entry", line_no, ":\t", line[0], "\t", line[13])
            line_no += 1
            if line[13] == "0.0":
                benign_list.append(format_string(line[0]) + "\n")
                out_legit += 1
            if line[13] == "1.0":
                phishing_list.append(format_string(line[0]) + "\n")
                out_phishing += 1

        print("\nTotal Legit:\t", out_legit, "\nTotal Phishing:\t", out_phishing)

        # Placing it into the file
        with open('SourceFiles/phishingLinks.txt', 'w') as file2:
            string_to_write = ''.join(phishing_list)
            file2.write(string_to_write)

        with open('SourceFiles/benignLinks.txt', 'w') as file3:
            string_to_write2 = ''.join(benign_list)
            file3.write(string_to_write2)


if __name__ == "__main__":
    generate_files()

# TODO: write code to preserve 1) the .com/.net etc, 2) have code preserve what comes after the .com i.e. /hello/you