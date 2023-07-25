#rewrote my old caesar cypher to accomdiate this challenge...
# shift = 3
import string

common_english = "ETAOIN SHRDLU" 
printable = string.ascii_letters.upper()

phrase = input("input cipher: ")
phrase = phrase.upper()

encrypt = []
#ascii values must stay between 65 - 90
#handles the 25 encryptions 
for y in range(26):
    val = []
    #x the amount to shift numbers in string
    for x in phrase:
        if ord(x) > 90 or ord(x) < 65:
            val.append(x)
        elif ord(x) == 32:
            val.append(" ")
        else: 
            x = chr(((ord(x) + 65) + y) % 26 + 65)
            val.append(x)
    encrypt.append((("rot "+ str(y)),''.join(val)))
    
## going to make this more instant by adding frequency analysis and tell
## which rotation is used
frequency = []

for x in encrypt:
    s = 0
    val = x[1]
    
    for y in val:
        if common_english.find(y) != -1:
            s += 1
    frequency.append((s,x))

sorted_elements = sorted(frequency, reverse=True)
for x in range(5):
    print(sorted_elements[x])