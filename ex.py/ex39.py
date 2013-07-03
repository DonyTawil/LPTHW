ten_things="motto android apple sony microsoft linux"
print("wait that makes 6 things not 10 let's fix this.")

stuff=ten_things.split(' ') #split(' ',things) i.e:split the items in things using ' ' (space)
more_stuff=['brain','mechatronics','backtrack','xbox360','ps3','laptop','ubuntu','toshiba','mazda','acad']

while len(stuff) != 10:
    next_one=more_stuff.pop()  #pop(more_stuff,) i.e pop the last thing in stuff
    print("Adding: ",next_one)
    stuff.append(next_one)    #append(stuff, next_one) i.e add next_one to stuff
    print("there are %d items now in stuff"%len(stuff))  

print("there we go",stuff)
print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))     #join(' ',stuff) i.e join all the items in stuff using ' ' between them
print('#'.join(stuff[3:5]))#join('#',stuff[3:5]) i.e join all the items starting form 3 ending at 4 with '#' between them
