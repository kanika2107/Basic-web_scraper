from urllib2 import urlopen,Request#Module for reading from the web

import sys  

reload(sys)  
sys.setdefaultencoding("ISO-8859-1")

request = Request("https://hues.empa.ch/index.php/Special:CargoTables/Technologies")
response = urlopen(request)
the_page = response.read()
theText = the_page.decode()

f = open("output.txt",'w')
f.write(theText)
