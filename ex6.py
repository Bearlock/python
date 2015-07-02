import urllib
import pickle

# Using pickle was interesting. What I got from it is that it is an easy way to
# serialize data (using pickle.dump()) and unserialize it (using pickle.load())
# this allows one to use the serialized data/variable in different Python scripts
# Kinda makes Python function in an object-oriented way from what I have read
openSite = urllib.urlopen( "http://www.pythonchallenge.com/pc/def/banner.p" )
bannerPickle = pickle.load ( openSite )

# This is a two line bit of code, but it is something I was not familiar with.
# Essentially the second line of the code below takes advantage of what is known
# as list comprehension. In Python, it allows you to concisely make a list, most
# of the time from another list. It joins an empty string to a list resulting
# from multiplying the two values in a tuple that came from a list of unpickled data
print "\nFinal solution:\n "

for lists in bannerPickle:
	print(''.join( x * y for x, y in lists))
	
# uncomment the 2 lines below to see what unpickled data looks like	
#for lists in bannerPickle:
#	print lists
	
