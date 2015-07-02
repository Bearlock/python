# urllib allows you to do some nifty stuff, it  treats a website
# like a file and lets you get different properties from it. 
import urllib
import re

# The regexes I use below are for capturing the next 'nothing' parameter
# and for capturing the solution to the puzzle. The loop below this 
# uses the captured number (using regexNumber) and appends it to the 
# base url. It continues until a solution is found. i is just a counter. 
baseURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
regexNumber = re.compile('\d')
regexString = re.compile('[a-z].html')
givenNumber = "12345"
solution =''
i = 0

while solution == '':
	openSite = urllib.urlopen(baseURL + givenNumber)
	
	i += 1
	content = openSite.readline()
	print content
	if regexString.findall(content):
		solution = content
	else:
		number = regexNumber.findall(content)
		givenNumber = ''.join(number)
		print baseURL + givenNumber
	
print "\nFinal solution: %r" % solution 
print "\nIt took %d tries" % i

# While not explicitly used in this solution, the functions below
# are handy, and were of great use to me in other endeavors. 
# openSite.info() - gets Mime-type headers
# openSite.geturl() - gets the url you opened
# openSite.getcode() - gets response code
