people=input('write number of people:')
cats=input('number of cats:')
dogs=input('number of dogs:')

people=int(people)
cats=int(cats)
dogs=int(dogs)

if people < cats:
   print ("too many cats! The world is doomed!")
if people < dogs:
   print ("the world is drooled on!")

if people > dogs:
   print ("the world is dry!")


dogs += 5

if people >= dogs:
   print ("People are greater than or equal to dogs")

if people <= dogs:
   print ("People are less than or equal to dogs")

if people == dogs:
   print ("People are dogs.")

if people>dogs and cats>dogs:
   print ("Dogs are doomed")

if people< dogs or people < cats:
   print ('we are outnumberd')

if not(people !=cats and dogs > cats):
   print ("the world is in an unknown state")
