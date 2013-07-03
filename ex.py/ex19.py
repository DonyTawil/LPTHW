#Create and define the function,and define the variables
def cheese_and_crackers(cheese_count, cracker_amount):
    print ("we have %d  cheese!"%cheese_count)
    print ("we have %d boxes of crackers!"%cracker_amount)
    print ("that is enough for a great party!!\n")
  
print ("we can give the functions numbers directly!")
#Gives immediatly the modules values
cheese_and_crackers(20,10)

print ("Or we can use variables from our script!")
#defining each module alone
cheese_count = 19
cracker_amount = 33
#Runs the function
cheese_and_crackers(cheese_count,cracker_amount)

print ('we can do math too!')
#Define the modules
cheese_and_crackers(6+15*2,25/5+13)
print ('we can even combine the too variables and do math too')
#And run it too
cheese_and_crackers(10+ cheese_count, 21+cracker_amount)
