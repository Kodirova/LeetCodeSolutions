import re
def valid():
    a =[]
    f = open("phone.txt", "r")
    for x in f:
        path = re.match('^\(\d{3}\)\s\d{3}-\d{4}', x)
        pathTwo = re.match('^\d{3}-\d{3}-\d{4}', x)

        if path or pathTwo :
            a.append(x)
    return a            

