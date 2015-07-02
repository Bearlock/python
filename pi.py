import math

def piDigit(nList, choice):
	if choice == 0:
		return nList[choice]
	elif choice == 1:
		return nList[choice - 1] + '.' + nList[choice]
	else:
		testString = "".join(nList[x] for x in range(1, choice + 1))
		return nList[0] + '.' + testString

number = math.pi
numberList = list()
numberString = str(number)

for digit in numberString:
	numberList.append(digit)

numberList.remove(".")
print "Hello, this short program outputs pi to the nth decimal up to the eleventh decimal.\n"

try:
	userChoice = int(raw_input("Please enter a number and I will print pi to that decimal >> "))
except ValueError:
	print "Not a number"

print "\n" + piDigit(numberList, userChoice) + "\n"

	
