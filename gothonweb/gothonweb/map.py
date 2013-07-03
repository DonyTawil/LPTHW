from maptext import*
import web
class Room(object):

    def __init__(self, name, description,ide=None,help=None,score=5):
        self.name = name
        self.score=score
        self.description = description
        self.paths = {}
        self.ide=ide #This is used for cheats and the game completion thingy
        self.score=5#this is the score won from each game
        help=str(help)# just in case help is still none
        self.help=help+"this is the help"

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
    

lwac=lwa+code

central_corridor = Room("Central Corridor",cc,1)

laser_weapon_armory = Room("Laser Weapon Armory",lwa,2)

escape_pod = Room("Escape Pod",ep,4)

escape_podc = Room("Escape Pod",definition,4)

the_bridge = Room("The Bridge",tb,3)

the_end_winner = Room("The End",tew,5)

the_end_loser = Room("The End",tel,5)

tbomb_death= Room("death",tbd,3)

bcode_death= Room("death",bcd,2)

shoot_death= Room("death",sd,1)

dodge_death= Room("death",dd,1)

laser_weapon_armoryc= Room("Laser Weapon Armory",lwac,2)




escape_pod.add_paths({
        '%d'%c : the_end_winner,
        'hey':escape_podc})
for e in range(1,6): #To assign all the remaining numbers
    if e == c:
        continue
    escape_pod.add_paths({
        '%d'%e:the_end_loser,
})

escape_podc.add_paths(escape_pod.paths)

the_bridge.add_paths({
    'throw the bomb': tbomb_death,
    'slowly place the bomb': escape_pod
})    





laser_weapon_armory.add_paths({
    code : the_bridge,
    'one':the_bridge,
    'you tell me': laser_weapon_armoryc,
    '*': bcode_death
})

laser_weapon_armoryc.add_paths(laser_weapon_armory.paths)

central_corridor.add_paths({
    'shoot!':shoot_death,
    'tell a joke': laser_weapon_armory,
    'dodge!':dodge_death
})


START = central_corridor
        
