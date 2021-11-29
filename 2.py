import re

datakey = ["dumb","ways","the","best"]
txt = "dumbways"

#Check if the string has any a, r, or n characters:
def check(datakey,word):
    for i in (datakey):
        x = re.findall(i,word)
        if x:
            print (x,"=>",bool(x))
        else:
            print ("Not match","=>",bool(x))

check(datakey,txt)