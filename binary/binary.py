with open("binary", 'bw') as bin_file:  # bw = binary write
    for i in range(17):
        bin_file.write(bytes([i]))  # bytes() converts the range into binary

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)