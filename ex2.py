def charShift(c):
    # List of punctuation checked in the if statement, returns punctuation if true
    punctuation = ["!", "@", "#", "$", "%", "^", "*", "(", ")", ".", "?", "'", " ", ",", "/"]
    
    if c in punctuation:
        return c
    else:
        # ord() takes a character and returns its ascii value
        # cnr() takes an ascii value and returns a character
        # in this way, we can shift a character by 2
        if ord(c) + 2 > ord('z'):
            return chr(ord(c) - 24)
        else:
            return chr(ord(c)+2)

# Original puzzle string
codedString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

# String to use after decoding coded string
codedString2 = "map"


#list() takes a string and can break it down into individual parts
stringList = list(codedString)
stringList2 = list(codedString2)
translatedString = ""
translatedString2 =""

for chars in stringList:
    l = charShift(chars)
    translatedString += l
    
for chars in stringList2:
	l2 = charShift(chars)
	translatedString2 += l2
    
print "\nOriginal message: " + translatedString + '\n'
print "\nFinal Solution: " + translatedString2 + ".html\n"

# Turns out the actual solution uses string.maketrans(), but I feel that this a pretty good solution too.
# You can definitely see my C++ heritage here with how I handle strings and chars.
# I probably could have turned the above chunk of code into its own function, but I feel that it was simple 
# enough that I could get away with copying. Any more, and I would have turned it into its own function.  