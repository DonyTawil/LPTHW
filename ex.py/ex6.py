# Defining variable with format.
x=('there are %d types of people.' %2)
# Defining variable
binary ='binary'
do_not="don't"
# defining variable with two formats.
y = "Those who know %s, and those who %s" %(binary, do_not)# string inside string.
#printing variables.
print (x)
print (y)
# printing phrase plus formatting variable
print ("I said: %r."%x)#string inside string
print ("I also said: '%s'." %y)#string inside string
# defining variable with the already defined False
hilarious = False
#Variable with format.
joke_evaluation = "Isn't this funny!!? %r"
#printing variable with other variable as format
print (joke_evaluation % hilarious)
#defining variable. 
w= "Left side, center "
e= "square, right side."
# adding two variables wich are strings.
print (w + e) #string inside string.
