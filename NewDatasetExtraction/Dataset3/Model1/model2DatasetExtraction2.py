import string


def remove_special_characters(input_string):
    special_characters = list(string.punctuation)
    new_string = ""
    for character in input_string:
        if character not in special_characters:
            new_string += character

    return new_string


def format_string_with_special_characters(input_string):
    return format_inner(input_string, 0)


def format_string(input_string):
    return format_inner(input_string, 1)


def format_inner(input_string, special_character_removal):
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

    print(split_string)

    # need to account for whether www. at the start (replacing subdomain with more relevant)
    # to make work for example www.users.waitrose.com (given in url set)
    if len(split_string) > 3:
        subdomain = split_string[0]
        second_level_domain = split_string[1]
        startpoint = 2
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

    if special_character_removal == 1:
        return remove_special_characters(subdomain), remove_special_characters(
            second_level_domain), remove_special_characters(top_level_domain), remove_special_characters(subdirectory)
    else:
        return subdomain, second_level_domain, top_level_domain, subdirectory


def generate_files(approach):
    with open('data.txt', mode='r') as file:
        list_of_lines = file.readlines()

        phishing_list_subdomain = []
        phishing_list_second_level_domain = []
        phishing_list_top_level_domain = []
        phishing_list_subdirectory = []
        benign_list_subdomain = []
        benign_list_second_level_domain = []
        benign_list_top_level_domain = []
        benign_list_subdirectory = []
        out_legit = 0
        out_phishing = 0

        for line in list_of_lines:

            if line.startswith("INSERT INTO"):
                # ignore
                print(line)
            else:

                line = line[1:len(line)-3]

                commasplit = line.split(",")
                index = commasplit[0]

                speechsplit = line[len(index):len(line)]

                speechsplit = speechsplit.split("'")
                url = speechsplit[1]
                url = url.split("://")[1]
                label = int(speechsplit[4][2:-2])

                print(url)

                subdomain_file, secondlevel_file, toplevel_file, subdirectory_file = format_string(url)

                # approach one wants a benignlinks.txt file and a phishinglinks.txt file.
                if approach == 1:
                    if label == 0:
                        benign_list_subdomain.append(subdomain_file + "\n")
                        benign_list_second_level_domain.append(secondlevel_file + "\n")
                        benign_list_top_level_domain.append(toplevel_file + "\n")
                        benign_list_subdirectory.append(subdirectory_file + "\n")
                        out_legit += 1
                    elif label == 1:
                        phishing_list_subdomain.append(subdomain_file + "\n")
                        phishing_list_second_level_domain.append(secondlevel_file + "\n")
                        phishing_list_top_level_domain.append(toplevel_file + "\n")
                        phishing_list_subdirectory.append(subdirectory_file + "\n")
                        out_phishing += 1

        print("\nTotal Legit:\t", out_legit, "\nTotal Phishing:\t", out_phishing)

        # Placing it into the file
        # Phishing
        with open('Model2/phishing_subdomain.txt', 'w') as phishing_subdomain:
            string_to_write_ps = ''.join(phishing_list_subdomain)
            phishing_subdomain.write(string_to_write_ps)

        with open('Model2/phishing_second_level_domain.txt', 'w') as phishing_second_level:
            string_to_write_psld = ''.join(phishing_list_second_level_domain)
            phishing_second_level.write(string_to_write_psld)

        with open('Model2/phishing_top_level_domain.txt', 'w') as phishing_top_level:
            string_to_write_ptld = ''.join(phishing_list_top_level_domain)
            phishing_top_level.write(string_to_write_ptld)

        with open('Model2/phishing_subdirectory.txt', 'w') as phishing_subdirectory:
            string_to_write_psd = ''.join(phishing_list_subdirectory)
            phishing_subdirectory.write(string_to_write_psd)

        # Benign
        with open('Model2/benign_subdomain.txt', 'w') as benign_subdomain:
            string_to_write_bs = ''.join(benign_list_subdomain)
            benign_subdomain.write(string_to_write_bs)

        with open('Model2/benign_second_level_domain.txt', 'w') as benign_second_level:
            string_to_write_bsld = ''.join(benign_list_second_level_domain)
            benign_second_level.write(string_to_write_bsld)

        with open('Model2/benign_top_level_domain.txt', 'w') as benign_top_level:
            string_to_write_btld = ''.join(benign_list_top_level_domain)
            benign_top_level.write(string_to_write_btld)

        with open('Model2/benign_subdirectory.txt', 'w') as benign_subdirectory:
            string_to_write_bsd = ''.join(benign_list_subdirectory)
            benign_subdirectory.write(string_to_write_bsd)


if __name__ == "__main__":
    generate_files(1)

