# shift = 3
phrase = "EVXFZO NHVMO KDIF MJVY"
encrypt = []
#ascii values must stay between 65 - 90
#handles the 25 encryptions 
for y in range(26):
    #x the amount to shift numbers in string
    for x in phrase:
        if ord(x) == 32:
            encrypt.append(" ")
        else: 
            x = chr(((ord(x) + 65) + y) % 26 + 65)
            encrypt.append(x)
    print(y," == " + ''.join(encrypt) + "")
    encrypt.clear()