cipher = input("Input your ceasar cipher: ")
cipher = cipher.upper() ## ascii range 65 - 90

ciphers = []
for x in range(1, 27):
    rotation = []
    for y in cipher:
        val = ord(y)
        if (val < 65 ) or (val > 90 ): ## if its not a char
            rotation.append(y)
        elif val == 32: 
            rotation.append(" ") ## if it's a white space
        else:
            rot_val = (((val + 90) + x) % 26) + 65 ## the meat 
            rotation.append(chr(rot_val))
    ciphers.append((f"rot {27 - x} " + "".join(rotation)))    
    
for x in ciphers:
    print(x)