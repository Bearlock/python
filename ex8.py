from PIL import Image
import urllib
import re

# This puzzle started interestingly. The puzzle page merely consisted of an image with a monochrome
# Bar running right through the middle of it. I assumed (after some time) that the bars had different
# RGB values, and that the answer to this puzzle would be encoded within those values. 

# We start as usual, retrieving a file with urllib
openSite = urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "/home/erick/public_html/ex8.png")

# Since the gray bar is smack dab in the middle of the image, I had to get the images size and divide
# by two along its width. This was done in order to use the getpixel() function from the image library
# it returns the numerical value for and (x,y) coordinate pair. using the getbands() function allowed
# me to glean that this photo had RGBA values. As such, when I used getpixel() it returned a four-tuple
im = Image.open("ex8.png")
size = im.size
length = size[0]
width = size[1] / 2

pixelList = list()

# I saved the first value of every tuple into a list called 'pixelList'. This was done so I could convert
# the values into characters later using the chr() function. The reason why I have my range incrementing 
# 7 is because the monochrome bands seem to change every 7 pixels or so. I imagine they are base 8. 
for x in range(0, length, 7):
	pixelTuple = im.getpixel((x,width))
	pixelList.append(pixelTuple[0])

charList = list()

# Converting the values into characters and saving them into a list
for pixel in pixelList:
	charList.append(chr(pixel))

# Here I convert the character list into a string and print it. Turns out the string had another list of values
# for me to parse through. I used a regex to get the 3 digit values, saved them to a list, and cast them into 
# int values using a list comprehension since they were originally strings. Apparently map() would work for this
# as well, but I didn't feel comfortable using something I don't know. I am not a fan of copy-paste code. 
# Note that the pixel string has 3 extra characters at the end. I could mitigate this by reducing the length variable
# in the first for-loop by 21, but that would make my code messier then it already is. I decided to not worry about it. 
pixelString = ''.join(charList)
regexNumber = re.compile("[\d]{3}")
found = regexNumber.findall(pixelString)
found = [int(number) for number in found]
finalList = list()

print "\n" + pixelString

# Here I use chr() on the values list to get the final answer
for numbers in found:
	finalList.append(chr(numbers))
	
finalString = ''.join(finalList)
print "\nFinal solution: " + finalString + "\n"

#print list(im.getdata())

# imageList = list(im.getdata())
# 
# for pixel in imageList:
# 	print pixel
	
#print im.histogram()
# print im.format
# print im.size
# print im.mode
# print im.palette
# print im.info
# print im.getbands()
# print im.getcolors()
# print im.getpixel((2, 48))