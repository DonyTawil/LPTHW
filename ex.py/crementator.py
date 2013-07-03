Python 3.1 (r31:73574, Jun 26 2009, 20:21:35) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """hello motto"
KeyboardInterrupt
>>> 
>>> def inc(fn,ln,step):
	fn=fn+step
	if fn <ln:
		inc(fn,ln,step)

		
>>> def dec(fn,ln,step):
	fn=fn-step
	if fn>ln:
		dec(fn,ln,step)

		
>>> def crementator(fn,ln,step):
	fn=0 ,ln=0 ,step=0
	
SyntaxError: can't assign to literal (<pyshell#18>, line 2)
>>> def crementator(fn,ln,step):
	print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	if fn<ln:
		inc(fn,ln,step)

		
>>> def crementator(fn,ln,step):
	print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	if fn<ln:
		inc(fn,ln,step)
	elif fn>ln
	
SyntaxError: invalid syntax (<pyshell#31>, line 11)
>>> def crementator(fn,ln,step):
	print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	if fn<ln:
		inc(fn,ln,step)
	elif fn>ln:
		dec(fn,ln,step)
	else:
		print("fn is equal to ln")

		
>>> crementator(fn,ln,step)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    crementator(fn,ln,step)
NameError: name 'fn' is not defined
>>> crementator(a,b,c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    crementator(a,b,c)
NameError: name 'a' is not defined
>>> def crementator(fn,ln,step):
	print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	if fn<ln:
		inc(fn,ln,step)
	elif fn>ln:
		dec(fn,ln,step)
	else:
		print("fn is equal to ln")

		
>>> print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	
please input first_number and last_number and step
>>> 10
10
>>> 100
100
>>> 1
1
>>> crementator(fn,ln,step)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    crementator(fn,ln,step)
NameError: name 'fn' is not defined
>>> print(fn)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(fn)
NameError: name 'fn' is not defined
>>> def start():
	print("please input first_number and last_number and step")
	fn=input("fn:")
	ln=input("ln:")
	step=input("step")
	fn=int(fn)
	ln=int(ln)
	step=int(step)
	crementator(fn,ln,step)

	
>>> start()
please input first_number and last_number and step
fn:30
ln:35
step1
please input first_number and last_number and step
fn:
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    start()
  File "<pyshell#50>", line 9, in start
    crementator(fn,ln,step)
  File "<pyshell#40>", line 3, in crementator
    fn=input("fn:")
KeyboardInterrupt
>>> def crementator(fn,ln,step):
	
	if fn<ln:
		inc(fn,ln,step)
	elif fn>ln:
		dec(fn,ln,step)
	else:
		print("fn is equal to ln")

		
>>> start()
please input first_number and last_number and step
fn:1
ln:10
step1
>>> def dec(fn,ln,step):
	fn=fn-step
        print(fn) 
	if fn>ln:
		dec(fn,ln,step)
		
SyntaxError: inconsistent use of tabs and spaces in indentation (<pyshell#55>, line 3)
>>> def dec(fn,ln,step):
	fn=fn-step
        print(fn)
	if fn>ln:
		dec(fn,ln,step)
		
SyntaxError: inconsistent use of tabs and spaces in indentation (<pyshell#56>, line 3)
>>> def dec(fn,ln,step):
	fn=fn-step
	print(fn)
	if fn>ln:
		dec(fn,ln,step)

		
>>> start()
please input first_number and last_number and step
fn:35
ln:30
step1
34
33
32
31
30
>>> 
