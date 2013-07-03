#create modules
from sys import argv
#assign modules to unpack
(script, filename)=argv
#assign the open function to txt 
print ("what is the name of your file")

txt = open(filename)
#print...
print ("here's your file %r yayyy!:"%filename)
#print the contents of written file
print (txt.read())
#print...
print ("type the filename again please!:")
#assign filename_ag function.
filename_ag = filename
#assign function again
txt_again = open(filename_ag)
#print the contents of written file
print (txt_again.read())
txt.close()
txt_again.close()

print (txt.close())
print (txt_again.close())
print (txt.closed)
print ((open('ex15_test.txt')).closed)
