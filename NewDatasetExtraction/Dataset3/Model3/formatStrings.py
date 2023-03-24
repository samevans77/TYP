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

    if special_character_removal == 1:
        return remove_special_characters(subdomain), remove_special_characters(
            second_level_domain), remove_special_characters(top_level_domain), remove_special_characters(subdirectory)
    else:
        return subdomain, second_level_domain, top_level_domain, subdirectory