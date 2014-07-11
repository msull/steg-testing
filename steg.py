# get multi-variable with statement
# support from python3
from __future__ import with_statement

base_image = "Original.bmp"
hidden_image = "secret.jpg"
output_file1 = "Hidden.bmp"

trans_dict = {
    "0": -8,
    "1": -7,
    "2": -6,
    "3": -5,
    "4": -4,
    "5": -3,
    "6": -2,
    "7": -1,
    "8": 1,
    "9": 2,
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6,
    "E": 7,
    "F": 8,
}

#main program logic here
with open(base_image, "rb") as base_file, \
    open(hidden_image, "rb") as hide_file, \
    open(output_file1, "wb") as out_file:
    
    # first, convert jpg into list of
    # hex values to hide in the bmp
    hex_vals = list()
    while True:
        # grab a byte from hide_file
        hide_byte = hide_file.read(1)
        # verify we have a byte -- if
        # not, we are done here
        if not hide_byte:
            break        
        # convert byte into plain
        # hex string of size 2,
        # stripping first two chars
        # (hex identifier -- 0x)
        # and zfill so that it prepends
        # a zero if the value is a
        # single digit - ie 0x0, 0x1
        hex_val = hex(ord(hide_byte))[2:].zfill(2)
        
        # append each character of the
        # hex byte to the list separately
        hex_vals.append(hex_val[0].upper())
        hex_vals.append(hex_val[1].upper())

    # now go through bmp and hide the values!
    
    # dump first 10000 bytes of base_file into out_file
    # to get past all the misc headers info
    out_file.write(base_file.read(10000))
    
    # go through all the jpg hex that needs hiding
    for hex_val in hex_vals:
        # translate hex character into corresponding
        # substituion value, ie A becomes +3,
        # 3 becomes -5, etc
        this_val = trans_dict[hex_val]
        
        while True:
            # read in next byte of bmp
            this_byte = base_file.read(1)
            if not this_byte:
                print("Ran out of bytes! Use smaller jpg or bigger bmp!")
                break
            # make sure adjusted byte value is within
            # proper range 0 >= val <= 255
            # if not, write the byte to the file
            # and try next byte
            if ord(this_byte) + this_val < 0 or ord(this_byte) + this_val >= 255:
                out_file.write(this_byte)
                continue
                
            # Adjusted byte is valid, write it
            out_file.write(chr(ord(this_byte) + this_val))
            break
    
    # write remainder of base image
    # into output file
    out_file.write(base_file.read())
        