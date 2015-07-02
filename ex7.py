import urllib
import zipfile
import re

i = 0
txt = ".txt"
commentString = ''
solution = ''
regexNumber = re.compile('\d')

openSite = urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip", "/home/erick/public_html/test.zip")

archiveName = open('./test.zip', 'rb')
zipped = zipfile.ZipFile(archiveName)
#print zipped.namelist()

# Give from readme file
fileName = "90052" + txt

while solution == '':
	commentString += zipped.getinfo(fileName).comment
	fileContents = zipped.read(fileName, 'r')
	number = regexNumber.findall(fileContents)
	i += 1
	
	if number:
		fileName = ''.join(number) + txt
	else:
		print "\nFinal solution: \n" + commentString
		solution = commentString	
		
print "\nIt took %d tries" % i

# This solution gets you to a page with a riddle

