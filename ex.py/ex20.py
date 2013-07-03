from sys import argv

(script,input_file)=argv
#define function and read
def print_all(f):
    print(f.read())
#def function: return to zero
def rewind(f):
    f.seek(0)
#print line displays given line number
def print_a_line(line_count,f):
    print (line_count, f.readline())
#open file
current_file = open(input_file)

print ("lets first print the whole file.\n")
#prints the file input_file
print_all (current_file)

print ("Now let's rewind, Kind of like a tape.")
#returns file to zero condition
rewind(current_file)

print ("Let's print three lines:")
#print line number and print line from text file
current_line=1
print_a_line(current_line,current_file)
#same only for 2nd line
current_line+= 1
print_a_line(current_line,current_file)
#same but for 3rd
current_line+= 1
print_a_line(current_line,current_file)

suppose=("this is it")
print (suppose)
