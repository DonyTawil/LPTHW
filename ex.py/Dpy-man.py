def p():
    input("press any button to continue")
#This is the hand-made Python d-dictionary.
#important not hey.append(a) is == to append(hey,a)
print("\t\t\t\tKeywords")
print("""
A:and append argv args as assert  
B:break  
C:class continue close closed 
D:def del  
E:elif else except exec 
F:finally from for  
G:global  
I:if import in input is
L:lambda len
N:not
O:open or
P:pass pop print 
R:raise read return
S:seek sorted split  sys
T:truncate try
W:while with write
Y:yield 
extra:rewind execfile readline tell str() with assert close self object sum dict .upper .lower .strip #for strings  _init__(for initialyse)  dir(gives all atributes and methods associated to an object)
=> means outputs""") 

p()
#a1=and
a1='and'
print('\n%s is a boolean short-circuit operator that returns true or false'%a1)
print('for example if a is true and b true a and b returns %s'%(1 and 1))
p()
#a2='apppend'
print('\nFor open we use \'a\' as append to add to a text file without overwriting.')
print("""for example:
if f=open('test.txt'),and b='\\ngood morning motto' and print(f.read()) gives:
hello
then if we write:
f=open('test.txt','a')
f.write(b)
f=open('test.txt')
print(f.read()) gives the response:
hello
good mornig motto

2nd way
array.append(x)
ex:
l=[]
l.append('e')
print(l)
['e']
""")
p()
#a3='argv'
print('argv is short for arguments to unpack when using from system import argv')
p()
#a4='args'
print('args is short for variables used in function ex: def func(args1,args2):')
p()
#a5 as
print('when as is used with import as renames the imported object, see when used with \'with\'')
print("""ex from sys import exit as h

def dead(a):
    print(a)
    h(0)

would be equivalent to 
def dead(a):
    print(a)
    exit(0)""")
p()
#a6 assert
print("""the assert function raises an assertion error if given condition not verified
ex:
assert 1==2,'there is an error'
would raise an assertion error displaying the following
traceback <most recent call last>:
  File \"Dpy-man.py\", Line 64, in <module>
    assert 1==2,'there is an error'
AssertionError: there is an error""")
p()
#b1 break
print("""The break loop can only be used with a for or while loop or with the try statement.
When used with a loop it terminates the nearest enclosing loop meaning the nearest loop that contained it
if used with the try stmnt, and this try stmnt contained a finally clause it executes the finally clause before terminating the loop.

ex:#the following program would:
for a in range of (0,100):
    a=a+1
    print(a)
    if a == 50:
        print('a is equal to 50')
        break
    else:
        print(a)

#would give the following output:
1
2
3
4
...
49
a is equal to 50
#and here the program would end""")

p()

#c1=class
print("""Defines class which has specific statements in it.

ex:
class vectors:
    def __init___(v,x,y)      #Be careful you must use __init__ in order to use class as used below Remember to do more research about this bc this is advanced
        v.i=x
        v.j=y

a=vectors(20,13)
print(a.i,a.j)
#would give the following output:

20 13""")
p()
#c2=continue
print("""The continue can only be used in loops and not inside a funtion or statement
and if finally clause exist in a try stmnt, this clause is executed before the continue.
Also the continue jumps to the nearest loop after executing the previous one 
If continue is in a for loop, the contine clause jumps back to the start of the loop

ex:

i=1
while i<10:
    i+=1
    print(i)
    continue
while i<50:
    i+=1
    print(i)
#would give this output:
2
3
4
5
...
10
11
12
13
...
47
48
49
50""")
p()
#c3=close
print("""this function closes an opened file:
ex
h=open('ex.txt')
print (h.read())
h.close()

note the close order saves the changes made to ex.txt""")
p()
#c4=closed
print("""this function test to see if closed:
ex 
h=open('ex.txt')
h.close()
print(h.closed)
#would return True""")
p()
#d1=def

print(""" Creates function with it's args

ex:
def h():
   function1
   function2""")
p()
#d2=del        
print("""The del function deletes the value of a variable and the values in lists        
ex:

a=50

del a
print(a) #would give error

apple=['h','k','l','e']

del apple[2]
print(apple)
#would print
['h','k','e']""")
p()
#e1=elif
print("""elif function used in an if statement to give another if 
ex
a=input('')
a=int(a)
if a>50:
    print(50-a)
elif a<0:
    print(-a)""")
p()
#e2=else
print("""else function nested in an if statement if all conditions not applied
ex
a=input('>')
a=int(a)
if a>0:
    print(a)
else:
    print(-a)""")
p()
#e3=except
print("""except function put in a try stmnt

ex:

a=input(':')
try:
    a=int(a)
except ValueError:
    print ('not good')


print(a)""")
p()
#e4=exec
print("""exec executes a string or an code object
ex
a="print('helooooooo')"
exec(a)
=>
helooooooooo""")



p()
#f1=finally:
print("""Finally function executes sets of instruction before terminating the try stmnt, 
note finally always nested in a try statement
i=50
try:
    i=i+4
finally:
    print(i)
=>
52
""")
p()
#f2=from
print("""from stmnt is used in import stmnt to specify location of import""")
p()
#f3=for
print("""for loop used as follows:
fruits=[apples,grapes,pear]
for fruit in fruits:
    print(fruit)

apples
grapes
pear""")
p()
#g=global
print("""declares a variable wich keep its value as defined by function
ex:
a=10
def f1():
    a=43
    print(a)
    =>43
def f2():
    print(a)
    =>10

#if we write

a=10
def f1():
    a=43
    print(a)
    =>43
def f2()
    print(a)
    =>43""")
p()
#I1=if
print("""if statement is a decision test that executes expression when specific condition is verified
ex
people =5
if people<10: 
    print('there are less than ten people')
else:
    print('there are more than ten people')""")

#I2=import
print("""import statements imports functions from modules
diffrent lexics
from module import* #import everythin in module
from module import function # imports specified function to execute function(parameters...)
import module #imports all the module to execute write the following: module.function(parameters...)
ex:
hjhj:
def h(a):
    print(a)
from hjhj import*
h('hey value')
#when running execute the module hjhj then executes h('hey value')
=> execution fo hjhj.py
'hey value')
""")
p()
#I3=in
print("""Used in for loops assign values from list to a variable
ex
earth=['tunisia','bangladesh','bangkock','lebanon']
for land in earth:
    print(land)
=>
tunisia
bangladesh
bangkock
lebanon""")
p()
#I4=is
print("""is is a boolean operator that returns true if same objects are compared you can also use is not
ex
x=5
y=x-3
print(x is y)
=> False""")


p()
#l1=Lambda
print(""" lambda is an anonymous function with only one expression
ex 
l= lambda a,b,c: a+b/c

print(l(4,3,3))
=>5""")
p()
#l2=length
print(""" len is a built-in-function that returns len of the object of type string or dictionary
integer have no length

ex:
print(len('hello motto %d'%5))
=>13""")
p()
#N=not
print(""" not is boolean type turns boolean into its contradiction and not, is not, not and""")
p()
#O1=open
print("""open is a built-in-function that opens a file for editing
ex
h=open('breakfeast.txt')
print(h.closed)
=>False""")
p()
#O2=or
print("""boolean ooperator...""")
p()

#P1=pass
print("""pass statement creates a null operation wich does nothing either for a function or a class

ex:

def nothing():
    pass #Nothing defined yet
""")

p()

#p2=pop


print(""" pop built-in function takes an element of index a from a list or array:

app=[ 'hello','what','is','up']
print(app[0])=> hello
a=app.pop(0)
print(a)=> hello
print(app[0])=> what
""")

#p3=print

print(""" built in function that displays message on screen""")

p()

#r1=raise
print(""" built in function that raises error message 

print('input a positive number')
a=input('>')
a=int(a)
if a >0:
    print("Thanks for cooperation")
else:
    raise RuntimeError("bad input")
# if input negative the following message is displayed:

Tracecback <most recent call last>:
  File "testing.py", line ..., in <module>
    raise RuntimeError("bad input")
RuntimeError: bad input""")
p()
#r2=read
print("""reads an already opend file:
#if do.txt contains fdfdfdfdfd
hf=open('do.txt')
print(hf.closed)
print(hf.read())
=>fdfdfdfdfdfdf""")
p()
#r3=return
print("""In function used to take variable change it and then return is with new value:
ex:
c=0
def add(a,b):
    return a+b
c=add(2,33)
print(c)

c= 35""")
p()
#s1=seek
print("""seek is a file objects that goes to specified position in a text file can be used to write at specified position:
#do.txt:12345hey


hf=open('do.txt')
hf.seek(5,0)     #goes to position 5 relative to starting position 0, 1 for current pos, 2 for end of file(in this case use -a a is the number)
print(hf.read(1)) #in read(i) i is the number of bytes to read
=>h
if opening file in 'a':append mode even after seek file goes to end of file after the first write order
'w':write mode truncates the file first""")
p()
#s2=sorted
print("""sorted is a built in function that returns lists or strings in a weirdly organized way


l=['h','a','b','e','hello','go on']
e='come on mate'
le=sorted(l)
e1=sorted(e)
print(le)
print(e1)

=>
['a','b','e','go on','h','hello']
[' ',' ','a','c','e','e','m','m','n','o','o','t']""")
p()
#s3=split
print(''''split is a built in function that splits phrase and puts it in list without the spaces
ex:
a='great day to be king'
c=a.split(" ")
print(c)
=>['great','day','to','be','king']''')
p()
#s4=sys
print(""" module file from wich we import functions""")
p()
#t1=truncate
print("""file objects wich deletes the text of the specified textfile
ex:
hf=open('do.txt','w')
hf.truncate(300)  #the specified number is the most that the file can contain (if file byte less depends on platform on mine fills it with spaces
hf.close()
hf=open('do.txt')
print(hf.read())
hf.close()
=>                                                                                                                                                                                                                      
""")
p()
#t2=try
print("""Try statement when encouters error searches for except clause and handles when it finds one it looks to see wether same error
ex:

print('please input number for test:')
x=input('>')
try:
   x=int(x)
   print(x+1)
except ValueError:
    print('wrong choice')
=>pleaase input number for test:23
24
""")
p()

#w1=while
print("""while stmnt is a loop that is executed while certain condition is verified
ex:
i=input(">")
10
while (i<50):
    i+=1
print(i)
50
""")
p()

#w2=with
print("""with stmnt to use a certain function multiple times
ex:
with open("do.txt") as a:
     print(a)
     a.read()
     print(a.read())
     a.close()
     print(a.closed)
=>
<_io.TextIOWrapper name='do.txt' encoding='cp1252'>
do.txt #prints the stuff in do.txt
""")
p()
#w3=write
print("""write built-in function used with the open function as:
a=open('textfile.txt',"r")
a.write('0')
=>#truncates the file
and writes in it 0""")
p()
#y1=yield 
print("""yield stmnt must be used in a generator it returns the value in the generator at each instance
such as in example:
def my_yield():
    for i in range (0,200):
        yield(i+i)
        
for b in my_yield(): #this is what you should type to get the result from first function
    print('this is b')
    print(b)
=>
this is b
2
this is b
4
.
.
.
this is b
398""")

p()
print("""\t\tDatatypes:
True
False
None
strings
numbers
floats 
lists""")

p()

print("True is a boolean Value it is the string equivalent of 1")
print("False is a boolean Value it is the string equiavalent of 0")
print("None is a single value that imply no data i.e it is the data returned when a function doesn't return a value")
print("string is the basic output it is what most of this program is made of")
print("Numbers are the following either integer 1 2 3 float 1.5 or complex i.e imaginary")
print("Floats are a type of number i.e 1.54")
print("lists are arrays that holds an object at a specific index")

p()

print("""\t\tEscape string sequences
\\
\t
\a
\'
\"
\v
\n
\r
\b
\f""")

print("\\\\ prints a backspace \\\' prints\' and \\\" prints \"")
print("\\t is for tab , \\a is for bell \\n is for newline")
print("\\b this is for backspace deletes last chracter, formfeed\\f should go to new page")
print("""and \\r is for end of line return to beginning of line 
ex:
print("hey\r1")
=>1ey""")
p()
print("""\t\tString formats:
%d  takes integer signed
%i  takes integer signed
%o  takes integer and returns its coordinates on base 8 ex 24 => 30 ((8**0)*0 + (8**1)*1)
%u  takes integer and represents it in decimal 10
%x  takes integer and represents it in hexadecimal
%X  takes integer and represents it in hexadecimal
%e  takes float xzcxzcx turns into x.zzcxzcxe*cv where e represents the number part and cv is the exponent of 10
%E  takes float xzcxzcx turns into x.zzcxzcxe*cv where e represents the number part and cv is the exponent of 10
%f  takes float and represents it with closest mantissa representation??
%F  takes float and represents it with closest mantissa representation??
%g  takes shortest of %e or %f
%G  takes shortest of %e or %f
%c  takes only character
%r  takes anything as anything using repr()
%s  takes string using str()
%%  prints %%?""")
p()

print("""\t\tOperators
/   does division
//  floor division wich gives the quotient without the decimal point
%   does modulo operation
<   test for less (displays true or false)
>   greater
<=  less or equal
>=  greater or equal 
==  test for equal
!=  test for diffrent
<>  ?
( ) creates 
[ ] creates list
{ } ?
@   used for functions and class methods @?
,   ?
:  creates function
.  uses specified operation example open("txt").write
=  assign value to variable
;  ?
+= incrementation operation
-= decrementation
*= * than equals
/= \ than equals 
//= floor division than equals 
%=  modulo than equals
**= exponent than equals""")
p()

print("""\t\t\tTerminology:
__init__ == initialise
self == method signature
The 'functions' that are part of an object are called methods.
You can examine all the methods and attributes that are associated with an object using the dir command :""")













