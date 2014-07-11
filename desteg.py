# get multi-variable with statement
# support from python3
from __future__ import with_statement

image1_file = "File1.bmp"
image2_file = "File3.bmp"

# in a more generic program, we would
# determine the output file extension
# after finding the hidden bytes
output_file1 = "output1.jpg"
output_file2 = "output2.jpg"

trans_dict = {
    -8: "0",
    -7: "1",
    -6: "2",
    -5: "3",
    -4: "4",
    -3: "5",
    -2: "6",
    -1: "7",
    1: "8",
    2: "9",
    3: "A",
    4: "B",
    5: "C",
    6: "D",
    7: "E",
    8: "F",
}

# couple of helper functions

def remap_values(values, trans):
    returnval = list()
    for val in values:
        returnval.append(trans[int(val)])
    return returnval

def write_hex2bin(output_filename, hex_values):
    hex_string = "".join(hex_values)
    with open(output_filename, "wb") as file_out:
        for x in xrange(0, len(hex_string), 2):
            file_out.write(chr(int(hex_string[x] + hex_string[x+1], 16)))
    

#main program logic here
with open(image1_file, "rb") as file1, open(image2_file, "rb") as file2:
    f1_sub_f2 = list()
    f2_sub_f1 = list()
    
    while True:
        # read a byte from each file and
        # verify they contain data (not EOF)
        f1_byte = file1.read(1)
        f2_byte = file2.read(1)
        if not f1_byte or not f2_byte:
            break
        f1_byte = ord(f1_byte)
        f2_byte = ord(f2_byte)
        if not f1_byte == f2_byte:
            f1_sub_f2.append(f1_byte - f2_byte)
            f2_sub_f1.append(f2_byte - f1_byte)
    
    write_hex2bin(output_file1, (remap_values(f1_sub_f2, trans_dict)))
    write_hex2bin(output_file2, (remap_values(f2_sub_f1, trans_dict)))
    
                