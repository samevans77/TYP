# https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset
# wanting to split the subdomain and second-level domain from the top-level domain.
import csv
from formatStrings import format_string


# opening the CSV file
def generate_files():
    with open('../../Data/urlset.csv', mode='r') as file:
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

        benign_list_additional_features = []
        phishing_list_additional_features = []
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
        with open('../../Data/phishing_subdomain.txt', 'w') as phishing_subdomain:
            string_to_write_ps = ''.join(phishing_list_subdomain)
            phishing_subdomain.write(string_to_write_ps)

        with open('../../Data/phishing_second_level_domain.txt', 'w') as phishing_second_level:
            string_to_write_psld = ''.join(phishing_list_second_level_domain)
            phishing_second_level.write(string_to_write_psld)

        with open('../../Data/phishing_top_level_domain.txt', 'w') as phishing_top_level:
            string_to_write_ptld = ''.join(phishing_list_top_level_domain)
            phishing_top_level.write(string_to_write_ptld)

        with open('../../Data/phishing_subdirectory.txt', 'w') as phishing_subdirectory:
            string_to_write_psd = ''.join(phishing_list_subdirectory)
            phishing_subdirectory.write(string_to_write_psd)

        # Benign
        with open('../../Data/benign_subdomain.txt', 'w') as benign_subdomain:
            string_to_write_bs = ''.join(benign_list_subdomain)
            benign_subdomain.write(string_to_write_bs)

        with open('../../Data/benign_second_level_domain.txt', 'w') as benign_second_level:
            string_to_write_bsld = ''.join(benign_list_second_level_domain)
            benign_second_level.write(string_to_write_bsld)

        with open('../../Data/benign_top_level_domain.txt', 'w') as benign_top_level:
            string_to_write_btld = ''.join(benign_list_top_level_domain)
            benign_top_level.write(string_to_write_btld)

        with open('../../Data/benign_subdirectory.txt', 'w') as benign_subdirectory:
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