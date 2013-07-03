print ("You enter a dark room with two doors. Do you choose door #1 or door #2?")

door = input('> ')

if door == '1':
   print ("there's a giant bear here eating a cheesecake. what do you do?")
   print ("1. Take the cake.")
   print ("2. Scream at the bear.")

   bear = input('> ')
   
   if bear == '1' or bear =='Take the cake.':
        print ('The bear eats your face off. Good job!')
   elif bear == '2':
        print (' the bear eats your legs off . Good job!')
   else:
        print ('Well, doing %s is probably better. Bear runs away.'% bear)

elif door == '2':
    print ('You stare into an endless abyss.')
    print ('1. You eat the blueberries that are on the floor.')
    print ('2. You take a yellow jacket that is on the ground and that seems to have magical properties.')
    print ('3. You take the gun\'s that you have found on the ground.')

    insanity = input('> ')

    if insanity == '1':
       print ('You feel your stomach burning, and then scream for help before you fall down and die! GOOD JOB!')
    elif insanity == '2':
        print('You feel the world around you blurr and your head get dizzy before founding yourself back at home safe and sound. Great job!!')
    elif insanity == '3':
        print ('A demon, offended, rushes at you in defence,and stabs you in the heart,before you can try to react. Job well done!!.')
    else:
        print ('You anger an ancient soul, causing it to attack and inhabit your body!')
        print ('\nYou struggle for control and manage to do wich of the following:!')
        print ('\n1. Control your body even though it is inhabitied.')
        print ('\n2. Kill yourself so that you may be free of the soul\'s grip')
        brain = input('>')
        if brain == '1':
            print('You succeed in controlling your body further angering the soul wich expells you from this hell and sends you back to your home safely.Great job!!!')
        elif brain == '2':
            print ('the demon\n leaves your body unscathed, you feel a deep cold, as your soul leaves your cadaver to wander in its turn this abyss for wich you will inhabit forever!!Job well done!')
        else:
            print ('Your actions are futile and the soul consumes your body, turning you into a mindless zombie!!! Job well done!')
        
print ('Game over!')
