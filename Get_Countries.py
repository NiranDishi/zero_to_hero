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
A2C=open("alpha2codes.txt","w+")



for i in range(len(data)): ## Going trough all the data list's length
    A2C = open("alpha2codes.txt", "a+" )  ## open alpha2codes file with an option to append a new values
    Dict=data[i]      ## Dict is contain the dictionery in data[i]'s list.
    Val=Dict.get("alpha2Code") ## Val is containing the value inside alpha2Coda's key.
    A2C.write("%s\r\n" % Val)  ##add to SUSKI file a new line with the alpha2Code's value
    A2C.close() ## close the file








