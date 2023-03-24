def convert_to_unicode(plaintext, total_length):
    output = ' '.join(format(ord(i), 'b') for i in plaintext)  # convert to bytes first. (7 bits)

    out_array = []
    for i in output.split(" "):
        out_array.append(int(i, 2))  # convert to an array of integers.
    for j in range(len(out_array), total_length):
        out_array.append(0)  # adds zeroes on for as many as necessary

    return out_array


if __name__ == '__main__':
    a = input("Input:")
    print(convert_to_unicode(a, 9))
