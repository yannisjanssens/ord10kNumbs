import os

count = 0
countTotal = 10000
while(count<=countTotal):
    f = open("files/"+str(count)+".txt", "w")
    f.write(str(count))
    count = count + 1
    f.close()
