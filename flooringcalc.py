def calc(p, l, w):
	area = l * w 
	total = area * p 
	return total


price = float(raw_input("\nHey, this is a flooring calculator, enter a price per square foot >> "))
length = int(raw_input("\nEnter the length of you area to the nearest foot >> "))
width = int(raw_input("\nEnter the width of your area to the nearest foot >> "))

calculatedArea = length * width
calculatedPrice = calc(price, length, width)

print "\nYour total area is {0} square feet and your total price is ${1:.2f}".format(calculatedArea, calculatedPrice)