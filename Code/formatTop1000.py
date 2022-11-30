#This data is taken from https://www.htmlstrip.com/alexa-top-1000-most-visited-websites
#This formatting data is only to do this specific operation to this website's output.
with open('./SourceFiles/alexaTop1000Websites.txt','r') as file:
    list_of_lines = file.readlines()

skipLine = False
new_lines_list = []

#taking every odd line
for line in list_of_lines:
    if(skipLine != True):
        skipLine = True
    else:
        print(line.strip())
        new_lines_list.append(line.strip()+"\n")
        skipLine = False

#Placing it into the file
with open('./SourceFiles/alexaTop1000Websites.txt','w') as file:
    string_to_write = ''.join(new_lines_list)
    file.write(string_to_write)