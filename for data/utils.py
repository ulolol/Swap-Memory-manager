def inttohex(int_):
    if int_ >= 0:
        return ("{0:0>4s}".format(hex(int_ % (1 << 16))[2:])).upper()
    else:
        return (hex((int_ + (1 << 16)) % (1 << 16)).upper()[2:]).upper()

def inttobin(int_):
    if int_ >= 0:
        return "{0:0>16s}".format(bin(int_)[2:])
    else:
        return bin((int_ + (1 << 16)) % (1 << 16)).upper()[2:]
    
def hextobin(hex_):
    return inttobin(int(hex_, 16))

def bintohex(bin_):
    return inttohex(int(bin_, 2))
