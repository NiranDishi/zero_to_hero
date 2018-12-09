########################################
############# NIRAN'S CODE #############
########################################

import requests # importing the requests library


# f= open("Susna.txt","w+")
# ## w+ the plus means if there wasnt any exist file Susna, then he will open a new one.
#
#
# for i in range(10):
#      f.write("This is line %d\r\n" % (i+1)) ## \r takes the cursor to the begining of line and print over there what inside the \r in that case\n.
#
# f.close()
#
# ##Im on Git baby!

############################################################


# api url
URL = "https://restcountries.eu/rest/v2/all"
r = requests.get(url=URL) ## r get the data inside him
# extracting data in json format
data = r.json()
SUSKI=open("SUSKI.txt","w+")





print(data)







