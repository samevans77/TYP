import numpy as np
from convertToUnicodeCode import convert_to_unicode as convert
from extractAdditionalFeatures import get_arrays

# open all files
# Phishing
with open("../../Data/phishing_subdomain.txt", 'r') as phishing_subdomain:
    phishing_subdomain_list_of_lines = phishing_subdomain.readlines()

with open("../../Data/phishing_subdirectory.txt", 'r') as phishing_subdirectory:
    phishing_subdirectory_list_of_lines = phishing_subdirectory.readlines()

with open("../../Data/phishing_second_level_domain.txt", 'r') as phishing_second_level_domain:
    phishing_second_level_domain_list_of_lines = phishing_second_level_domain.readlines()

with open("../../Data/phishing_top_level_domain.txt", 'r') as phishing_top_level_domain:
    phishing_top_level_domain_list_of_lines = phishing_top_level_domain.readlines()

# Benign
with open("../../Data/benign_subdomain.txt", 'r') as benign_subdomain:
    benign_subdomain_list_of_lines = benign_subdomain.readlines()

with open("../../Data/benign_subdirectory.txt", 'r') as benign_subdirectory:
    benign_subdirectory_list_of_lines = benign_subdirectory.readlines()

with open("../../Data/benign_second_level_domain.txt", 'r') as benign_second_level_domain:
    benign_second_level_domain_list_of_lines = benign_second_level_domain.readlines()

with open("../../Data/benign_top_level_domain.txt", 'r') as benign_top_level_domain:
    benign_top_level_domain_list_of_lines = benign_top_level_domain.readlines()

phishing_length = 0
benign_length = 0

max_subdomain_length = 0
max_subdirectory_length = 0
max_second_level_domain_length = 0
max_top_level_domain_length = 0

# detecting the largest length of subdomain
for line in benign_subdomain_list_of_lines:
    if len(line) > max_subdomain_length:
        max_subdomain_length = len(line)
    benign_length += 1

for line in phishing_subdomain_list_of_lines:
    if len(line) > max_subdomain_length:
        max_subdomain_length = len(line)
    phishing_length += 1

# subdirectory
for line in benign_subdirectory_list_of_lines:
    if len(line) > max_subdirectory_length:
        max_subdirectory_length = len(line)

for line in phishing_subdirectory_list_of_lines:
    if len(line) > max_subdirectory_length:
        max_subdirectory_length = len(line)

# second level domain
for line in benign_second_level_domain_list_of_lines:
    if len(line) > max_second_level_domain_length:
        max_second_level_domain_length = len(line)

for line in phishing_second_level_domain_list_of_lines:
    if len(line) > max_second_level_domain_length:
        max_second_level_domain_length = len(line)

# top level domain
for line in benign_top_level_domain_list_of_lines:
    if len(line) > max_top_level_domain_length:
        max_top_level_domain_length = len(line)

for line in phishing_top_level_domain_list_of_lines:
    if len(line) > max_top_level_domain_length:
        max_top_level_domain_length = len(line)

print("Total phishing data points:\t", phishing_length, "\nTotal benign data points:\t", benign_length)
print("Max length:\nSubdirectory:\t", max_subdirectory_length,"\nSubdomain:\t\t", max_subdomain_length,
      "\nSecond Level:\t", max_second_level_domain_length, "\nTop Level:\t\t", max_top_level_domain_length,
      "\nAdditional Features:\t7")


def create_subdomain_array():
    print("Creating subdomain data...")
    output = []

    for line_in in phishing_subdomain_list_of_lines:
        output.append(convert(line_in, max_subdomain_length) + [1])

    for line_in in benign_subdomain_list_of_lines:
        output.append(convert(line_in, max_subdomain_length) + [0])

    return np.array(output)


def create_second_level_array():
    print("Creating second-level domain data...")
    output = []

    for line_in in phishing_second_level_domain_list_of_lines:
        output.append(convert(line_in, max_second_level_domain_length) + [1])

    for line_in in benign_second_level_domain_list_of_lines:
        output.append(convert(line_in, max_second_level_domain_length) + [0])

    return np.array(output)


def create_top_level_array():
    print("Creating top-level domain data...")
    output = []

    for line_in in phishing_top_level_domain_list_of_lines:
        output.append(convert(line_in, max_top_level_domain_length) + [1])

    for line_in in benign_top_level_domain_list_of_lines:
        output.append(convert(line_in, max_top_level_domain_length) + [0])

    return np.array(output)


def create_subdirectory_array():
    print("Creating subdirectory data...")
    output = []

    for line_in in phishing_subdirectory_list_of_lines:
        output.append(convert(line_in, max_subdirectory_length) + [1])

    for line_in in benign_subdirectory_list_of_lines:
        output.append(convert(line_in, max_subdirectory_length) + [0])

    return np.array(output)


def create_additional_feature_array():
    print("Creating additional features...")

    phishing_additional_output, benign_additional_output = get_arrays()
    return np.concatenate((phishing_additional_output, benign_additional_output))


if __name__ == "__main__":
    # creates the single feature matrix containing the values of all the phishing and benign outputs.
    # print(create_url_array())
    # creates the label matrix for this.
    # print(create_phishing_array())
    print(create_additional_feature_array())

    # FOR NOW, APPENDING THE LABEL ON THE END SO THAT SHUFFLING WILL BE A LOT LESS PAINFUL
