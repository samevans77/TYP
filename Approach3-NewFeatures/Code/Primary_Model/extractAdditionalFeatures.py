# using : Intelligent rule-based phishing websites classification (Mohammad Et al.)
# from : Phishing Webpage Classification via Deep Learning-Based Algorithms: An Empirical Study
import re
import csv
import numpy as np
from formatStrings import format_string_with_special_characters as format_string_wsc
dictionaryURLService = {"bit": "ly", "tinyurl": "com", "ow": "ly", "srt": "gy"}
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# 1 denotes benign
# 0 denotes suspicious
# -1 denotes Phishing


def extract_additional_features(input_url, label, verbose):
    output_array = []

    if verbose:
        print(input_url)

    # feature 1: having ip address in url
    ip_match = re.search(ip_pattern, input_url)
    if ip_match:
        ip_address = ip_match.group(0)
        if verbose:
            print("IP In URL -", ip_address, "- phishing")
        output_array.append(-1)
    else:
        if verbose:
            print("No IP in URL - benign")
        output_array.append(1)

    # feature 2: url length
    if len(input_url) > 74:
        if verbose:
            print("Long url - phishing")
        output_array.append(-1)
    elif len(input_url) < 54:
        if verbose:
            print("Short url - benign")
        output_array.append(1)
    else:
        if verbose:
            print("Medium-sized url - suspicious")
        output_array.append(0)

    # feature 3: shortening url service
    subdomain, secondlevel, toplevel, subdirectory = format_string_wsc(input_url)

    if secondlevel in dictionaryURLService.keys():
        if toplevel == dictionaryURLService[secondlevel]:
            if verbose:
                print("IS a shortened url - phishing")
            output_array.append(-1)
        else:
            output_array.append(-1)  # TODO: This is clearly not right currently, review failing data
    else:
        if verbose:
            print("Not a shortened url (that we know of) - benign")
        output_array.append(1)

    # feature 4: having @ symbol
    if "@" in input_url:
        if verbose:
            print("Contains @ - phishing")
        output_array.append(-1)
    else:
        if verbose:
            print("Does not contain @ - benign")
        output_array.append(1)

    # feature 5: // for redirection
    if "//" in input_url:
        if verbose:
            print("Contains // - suspicious")
        output_array.append(-1)
    else:
        if verbose:
            print("Does not contain // - benign")
        output_array.append(1)

    # feature 6: adding a prefix or suffix separated by - to the domain
    if "-" in subdomain or "-" in toplevel or "-" in secondlevel:
        if verbose:
            print("Contains dash - suspicious")
        output_array.append(-1)
    else:
        if verbose:
            print("Does not contain dash - benign")
        output_array.append(1)

    # feature 7: sub-domain and multi sub-domains
    dot_count = 0
    for character in input_url:
        if character == ".":
            dot_count += 1

    if dot_count < 3:
        if verbose:
            print("Contains less than 3 dots - benign")
        output_array.append(1)
    elif dot_count == 3:
        if verbose:
            print("Contains 3 dots - suspicious")
        output_array.append(0)
    else:
        if verbose:
            print("Contains more than 3 dots - phishing")
        output_array.append(-1)

    output_array.append(label)

    if len(output_array) == 8:
        if verbose:
            print("Output array of correct length")
        return output_array
    else:
        print("[ERROR]: Output array in additional feature extraction not of recognised length")
        print(output_array)
        print(input_url)
        return 0


def get_arrays():
    with open('../../Data/urlset.csv', mode='r') as file:
        # reading the CSV file
        csv_file = csv.reader(file)
        line_no = 2
        benign_list_additional_features = []
        phishing_list_additional_features = []
    # displaying the website URLs
        for line in csv_file:
            line_no += 1
            if line[13] == "0.0":
                benign_list_additional_features.append(extract_additional_features(line[0], 0, False))
            if line[13] == "1.0":
                phishing_list_additional_features.append(extract_additional_features(line[0], 1, False))

    return np.array(phishing_list_additional_features), np.array(benign_list_additional_features)


if __name__ == "__main__":
    # inputstring = "https://portal.lancaster.ac.uk/intranet/news"
    # out = extract_additional_features(inputstring, 0, True)
    # print(out)
    bl, pl = get_arrays()
    print(bl)
    print(pl)
    print(extract_additional_features("premierpaymentprocessing.com/includes/boleto-2via-07-2012.php", -1, True))
