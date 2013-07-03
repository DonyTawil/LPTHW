from sys import argv

(script, filename)=argv

print ("we are going to erase %r."%filename)
print ("if you don't want that, hit CTRL-C.")
print ("if you do want that, Hit ENTER.")

input('? ')

print ("opening the file ...")
target=open(filename, 'w')

print ("Truncating the file. Goodbye!!")
target.truncate()

print ("Now I am going to ask you for three lines.")

Line_1 = input("Line 1: ")
Line_2 = input("Line 2: ")
Line_3 = input("Line 3: ")

print ("Now we will write these to the file.")

target.write("%r%s%r%s%r"%(Line_1,"\n",Line_2,"\n",Line_3))
target.write("\n")
target.write(Line_2)
target.write("\n")
target.write(Line_3)

print ("And finally we close it.")
target.close()
print (target.closed)
print ("Job well done!")
