# shift = 3
phrase = "xqkwKBN{z0bib1wv_l3kzgxb3l_70k23n2n}".upper()

encrypt = []
#ascii values must stay between 65 - 90
#handles the 25 encryptions 
for y in range(26):
    #x the amount to shift numbers in string
    for x in phrase:
        if ord(x) > 90 or ord(x) < 65:
            encrypt.append(x)
        elif ord(x) == 32:
            encrypt.append(" ")
        else: 
            x = chr(((ord(x) + 65) + y) % 26 + 65)
            encrypt.append(x)
    print(y," == " + ''.join(encrypt) + "")
    encrypt.clear()