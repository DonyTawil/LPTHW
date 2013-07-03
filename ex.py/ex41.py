from sys import exit
from random import randint

def death():
    quips=["You died. You kinda suck at this.","Dude you're shit!!","Nice job,you died ...jackass.","Akaaaaal.","Oh no!!You got your head blown off"]
    print (quips[randint(0, len(quips)-1)])
    exit(1)

def central_corridor(action):
    """The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.
\n
You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory"""

    if "shoot" in action:
        print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
        print("His clown costume is flowing and moving around his body, wich throw")
        print("off your aim. Your laser hits his costume but misses him entirely. This")
        print("completely ruins his brand new costume his mother bought wich")
        print("makes him fly into an insane rage and blast you repeatedly in the face until")
        print("you are dead. then he eats you.")
        return 'death'


    elif action =="dodge":
        print("Like a world class boxer you dodge, weave, slip and slide right")
        print("as the Gothon's blaster cranks a laser past your head.")
        print("In the middle of your artful dodge your foot slips and you")
        print("bang your head on the metal wall and pass out.")
        print("you wake up shortly afeter only to die as the gothon stomps on.")
        print("your head and eats you.")
        return 'death'

    elif (action =="tell a joke" or action=='j') :
        print("Lucky for you they made you learn Gothon insults in the academy.")
        print("you tell the one Gothon joke you know:")
        print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gyr ubhfr, fur fvgf neghaq gur ubhfr.")
        print("the gothon stops, tries not to laugh, then busts out laughing and can't move.")
        print("While he's laughing you run up and shoot him square in the head")
        print("putting him down, the jump through the Weapon Armory door.\n")
        return 'laser_weapon_armory'
    
    else:
        print("DOES NOT COMPUTE!")
        return 'central_corridor'

def laser_weapon_armory(guess):
    """you do a dive roll into the Weapon Armory, crouch and scan  the room
for more Gothons that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box
and you need the code to get the bomb out. if you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits."""
    code = "%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))


    guesses = 0

    while guess != code and guesses < 10:
        if guess == ('hey jude'):
            print("%r"%code)
            guess = input("[Keypad]> ")
            continue
        print("BZZZZEDD!")
        guesses += 1
        guess = input("[Keypad]> ")
        
        
    if guess == code:
        print("The container clicks open and the seal breaks, letting gas out.")
        print("you grab thee neutron bomb and run as fast as you can to the")
        print("bridge where you must place it in the right spot.\n")
        return 'the_bridge'
    

    else:
        print("The lock buzzes one last time and the you hear a sickening")
        print("melting sound as the mechanism is fused together.")
        print("you decide to sit there, and finally the Gothons blow up the")
        print("ship from their ship and you die.")
        return 'death'

def the_bridge(action):
    """You burst onto the bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their
weapons out yet, as the see the active bomb under you
arm and don't want to set it off."""
    


    if action == "throw the bomb":
        print("In a panic you throw the bomb at the group of Gothons")
        print("and make a leap for the door. Right as you drop it a")
        print("Gothon shoots you right in the back killing you.")
        print("As you die you see another Gothon frantically try to disamr")
        print("the bomb. you die knowing they will probably blow up when")
        print("it goes off.")
        return 'death'

    elif (action == "slowly place the bomb"
    or action == 'j') :
        print("You point your blaster at the bomb under your arm")
        print("and the Gothons put their hands up and start to sweat.")
        print("You inch backward to the door, open it, and then carefully")
        print("place the bomb on the floor, pointing your blaster at it.")
        print("You then jump back through the door, punch the close button")
        print("and blast the lock so the Gothons can't get out.")
        print("Now that the bomb is placed you run to the escape pod to")
        print("get off this tin can.\n")
        return 'escape_pod'
    else:
        print("DOES NOT COMPUT!")
        return "the_bridge"

def escape_pod(guess):
    """You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It seems like
Hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and
now need to pick one to take. Some of them could be damaged
but you don't have time to look. There's 5 pods, wich one
do you take?"""

    good_pod = randint(0,5)

    
    if guess == 'you tell me':
        print("%s"%good_pod)
        guess = input("[pod #]> ")
    if int(guess) != good_pod:
        print("You jump into pod %s and hit the eject button."%guess)
        print("The pod escapes out into the void of space, then")
        print("implodes as the hull ruptures, crushing your body")
        print("into jam jelly")
        return 'death'
    else:
        print("You jump into pod %s and hit the eject button."%guess)
        print("The pod easily slides out into space heading to")
        print("the planet below.  As it flies to the planet, you look")
        print("back and see your ship implode and then explode like a")
        print("bright star,  taking out the Gothon ship at the same")
        print("time.  You won!")
        exit(0)


ROOMS = {
         'death': death,
         'central_corridor':central_corridor,
         'laser_weapon_armory': laser_weapon_armory,
         'the_bridge':the_bridge,
         'escape_pod':escape_pod
         }

def runner(map,start):
    next = start

    while True:
        room = map[next]
        print(room)
        print("\n--------")
        print(room.__doc__)
        action=input(">")
        next = room(action)

runner(ROOMS, 'central_corridor')
        




    
