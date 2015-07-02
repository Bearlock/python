import json
import urllib

from pprint import pprint

openSite = urllib.urlretrieve("http://www.omdbapi.com/?t=What+a+girl+wants&plot=short&r=json", "./test.json")

with open('test.json') as data_file:
	data = json.load(data_file)
	
pprint(data)