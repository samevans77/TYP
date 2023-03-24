# https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset
# wanting to split the subdomain and second-level domain from the top-level domain.
import csv
import string


def remove_special_characters(input_string):
    special_characters = list(string.punctuation)
    new_string = ""
    for character in input_string:
        if character not in special_characters:
            new_string += character

    return new_string


def format_string(input_string):

    # take any given string, format it (removing https, www.)
    if input_string.startswith("'"):
        input_string = input_string[1:]  # removes the ' which some parts of the dataset includes.

    if input_string.endswith("'"):
        input_string = input_string[:-1]

    # split by subdomain, second-level domain and top-level domain
    split_string = input_string.split("/")[0]
    subdirectory = ""

    for j in range(1, len(input_string.split("/"))):
        subdirectory += input_string.split("/")[j]

    split_string = split_string.split(".")
    # need to scan for subdomain.
    subdomain = ""
    startpoint = 1

    # need to account for whether www. at the start (replacing subdomain with more relevant)
    # to make work for example www.users.waitrose.com (given in url set)
    if len(split_string) > 3:
        subdomain = split_string[1]
        second_level_domain = split_string[2]
        startpoint = 3
    elif len(split_string) == 3:
        subdomain = split_string[0]
        second_level_domain = split_string[1]
        startpoint = 2
    else:
        second_level_domain = split_string[0]
        startpoint = 1

    top_level_domain = ""

    for i in range(startpoint, len(split_string)):
        top_level_domain += split_string[i]

    # want to return an output tuple of {subdomain, secondLevel, toplevel, subdirectory} form with special characters
    # removed:

    return remove_special_characters(subdomain), remove_special_characters(second_level_domain), remove_special_characters(top_level_domain), remove_special_characters(subdirectory)


# opening the CSV file
def generate_files():
    with open('../Data/urlset.csv', mode='r') as file:
        # reading the CSV file
        csv_file = csv.reader(file)
        line_no = 2
        out_phishing = 0
        out_legit = 0
        phishing_list_subdomain = []
        phishing_list_second_level_domain = []
        phishing_list_top_level_domain = []
        phishing_list_subdirectory = []
        benign_list_subdomain = []
        benign_list_second_level_domain = []
        benign_list_top_level_domain = []
        benign_list_subdirectory = []
    # displaying the website URLs
        for line in csv_file:
            print("Entry", line_no, ":\t", line[0], "\t", line[13])
            line_no += 1
            subdomain_file, secondlevel_file, toplevel_file, subdirectory_file = format_string(line[0])
            if line[13] == "0.0":
                benign_list_subdomain.append(subdomain_file + "\n")
                benign_list_second_level_domain.append(secondlevel_file + "\n")
                benign_list_top_level_domain.append(toplevel_file + "\n")
                benign_list_subdirectory.append(subdirectory_file + "\n")
                out_legit += 1
            if line[13] == "1.0":
                phishing_list_subdomain.append(subdomain_file + "\n")
                phishing_list_second_level_domain.append(secondlevel_file + "\n")
                phishing_list_top_level_domain.append(toplevel_file + "\n")
                phishing_list_subdirectory.append(subdirectory_file + "\n")
                out_phishing += 1

        print("\nTotal Legit:\t", out_legit, "\nTotal Phishing:\t", out_phishing)

        # Placing it into the file
        # Phishing
        with open('../Data/phishing_subdomain.txt', 'w') as phishing_subdomain:
            string_to_write_ps = ''.join(phishing_list_subdomain)
            phishing_subdomain.write(string_to_write_ps)

        with open('../Data/phishing_second_level_domain.txt', 'w') as phishing_second_level:
            string_to_write_psld = ''.join(phishing_list_second_level_domain)
            phishing_second_level.write(string_to_write_psld)

        with open('../Data/phishing_top_level_domain.txt', 'w') as phishing_top_level:
            string_to_write_ptld = ''.join(phishing_list_top_level_domain)
            phishing_top_level.write(string_to_write_ptld)

        with open('../Data/phishing_subdirectory.txt', 'w') as phishing_subdirectory:
            string_to_write_psd = ''.join(phishing_list_subdirectory)
            phishing_subdirectory.write(string_to_write_psd)

        # Benign
        with open('../Data/benign_subdomain.txt', 'w') as benign_subdomain:
            string_to_write_bs = ''.join(benign_list_subdomain)
            benign_subdomain.write(string_to_write_bs)

        with open('../Data/benign_second_level_domain.txt', 'w') as benign_second_level:
            string_to_write_bsld = ''.join(benign_list_second_level_domain)
            benign_second_level.write(string_to_write_bsld)

        with open('../Data/benign_top_level_domain.txt', 'w') as benign_top_level:
            string_to_write_btld = ''.join(benign_list_top_level_domain)
            benign_top_level.write(string_to_write_btld)

        with open('../Data/benign_subdirectory.txt', 'w') as benign_subdirectory:
            string_to_write_bsd = ''.join(benign_list_subdirectory)
            benign_subdirectory.write(string_to_write_bsd)


if __name__ == "__main__":
    generate_files()

    # subdomain, secondLevel, toplevel, subdirectory = format_string("www.cadcam.solutionsaustralia.com.au/esticad.htm")
    #
    # print(subdomain)
    # print(secondLevel)
    # print(toplevel)
    # print(subdirectory)

# TODO: write code to preserve 1) the .com/.net etc, 2) have code preserve what comes after the .com i.e. /hello/you