from sys import exit

def gold_room():
    print ('This room is full of gold. How much do you take?')

    next = input('> ')
    try:
        next =int(next)
    except ValueError:
        dead('Man, Learn to type a number.') 
    else:
        how_much = int(next)

    if how_much < 50:
        print('Nice ,you\'re not greedy, you win!')
        exit(0)
    else:
        dead('you greedy bastard')


def bear_room():
    print('''there is aa bear here.
    The bear has a bunch of honey.
    the fat bear is in front of another door.
    how are you going to move the bear?''')
    bear_moved = False

    for_bear()

def cthulu_room():
    print ("""here you see the great evil Cthulu.
    he, is, whatever stares at you and you go insane.
    do you flee for your life or eat your head?""")
   
    next= input('>')
    if 'flee' in next:
        start()
    elif 'head' in next:
        dead('well that was nasty!')
    else:
        cthulu_room()

def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print(""" You are in a dark room.
    there is a door to your right and left.
    which one do you take?""")

    next = input('>')
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

def for_bear():
    next = input('>')

    if next == 'take honey':
        dead('the bear looks at you then slaps your face off.')
    elif next == 'taunt bear' and not bear_moved:
        print ('the bear has moved from the door. You can go through here now.')

        bear_moved = True
    elif next == 'taunt bear' and bear_moved:
        dead('the bear gets pissed off and chews your leg off.')
    elif next == 'open door' and bear_moved:
        gold_room()
    else:
        print('I have no idea what that means')
        for_bear()



start()
#take stuff from test2 to complete extra credit then try to find out what the hell is this for """ fjdkfjdfljk"""
