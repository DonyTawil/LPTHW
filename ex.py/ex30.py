people=input('people:')
people=int(people)
cars=input('cars:')
cars=int(cars)
buses=input('buses:')
buses=int(buses)


if cars>people and people<buses:
   print('we should take the cars and the buses')
elif cars <people and buses> people:
    print ('we should not take the cars but only the buses')
elif cars >people and buses<people:
    print('we should only take the cars and a couple of buses')
else:
    print('we can\'t decide.')
if buses>cars and people>buses:
   print('that\'s too many people.Buy more BUSES!!!.')
elif buses<cars and people>cars :
    print('That\'s too many people.Buy more CARS!!')
else:
    print ('we still can\'t decide.')

if people==buses and cars==buses:
    print('Alright,we are in equilibrium nobody break a bus or a car.')

