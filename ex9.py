import bz2
import urllib
import re

# This Python challenge involved using bzip2 to decompress strings of data that
# were provided in the page's source. These strings act as a username and password
# to access the next level. 
openSite = urllib.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html")
regexBytes = re.compile("BZ.*")
siteContent = openSite.read()

bytesList = regexBytes.findall(siteContent)

# The regex above grabbed exactly what I needed, except since its greedy and I have
# limited experience writing good ones, it included an extra quote character that
# I don't need. Python's slice feature comes in handy here. 
byteUsername = bytesList[0]
bytePassword = bytesList[1]

byteUsername = byteUsername[0:-1]
bytePassword = bytePassword[0:-1]

# The format of the compression is bz2. The hint here was that the beginning of 
# compressed bz2 strings start with 'BZ'. This was useful for the regex. 
# A raw string is not compatible with this decompression, so the string has to
# be decoded with a string_escape, otherwise it throws a data stream error. 
username = bz2.decompress(byteUsername.decode('string_escape'))
password = bz2.decompress(bytePassword.decode('string_escape'))

print "\nFinal solution:\n"
print "\tUsername: %r" % username
print "\tPassword: %r\n" % password
