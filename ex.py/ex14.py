from sys import argv

(script, user_name,l_name)=argv
prompt=('type awnser here: ')

print ("Hello %s, I am the %s script."%(user_name,script))
print ("I'm going to ask you a few question.")
print ("Do you like me %s %s?"%(user_name,l_name))
likes = input (prompt)

print ("Where do you live Mr.%s?"%user_name)
lives = input (prompt)
print("what kind of cp do you have?")
computer = input (prompt)

print("""
so you said %s about liking me
you also said that you live in %s.
and that your computer is %s"""%(likes, lives, computer))
