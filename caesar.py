#rewrote my old caesar cypher to accomdiate this challenge...
# shift = 3
import string

common_english = "ETAOIN SHRDLU" 
printable = string.ascii_letters.upper()

phrase = input("input cipher: ")
phrase = phrase.upper()

encrypt = []
"""
This is the implementation of the decryption function for Caesar Cipher. 
With the help of modular arithmetic, we are able to wrap around the ascii letters
so we can execute this correctly. 

Im going to take input and make it uppercase, thus its ascii range will be 65-90. 
This will make programming this much easier.
"""

#ascii values must stay between 65 - 90
#handles the 25 encryptions 
for y in range(26):
    val = []
    #x the amount to shift numbers in string
    for x in phrase:
        if ord(x) > 90 or ord(x) < 65: ## this is checking to see if its a non character
            val.append(x)
        elif ord(x) == 32: ## if its white space
            val.append(" ")
        else: ## the SAUCE
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