from sys import exit

def c():
    input('Press any key to continue')

def hf():
    print('A monster comes running and screaming at you what do you do')
    action=input('>')
    if 'flee' in action or 'run' in action:
        print('the monster catches up to you and eats your face off')
        dead('that was shit.')
    elif 'crowbar' in action:
        print('you raise your crowbar and bash the monster on the head with it.\nyou throw the crowbar on the floor.\nAll of a sudden you feel everything blur around you then you find yourself in hell')
        c()
        hell()  
    else:
        print('The monster overcomes your moves and eats your face')
        dead('that was weak')

def hell():
    print('\nyou look around, and you find everything in flames, you hear lots of screaming. then you see a small man staring you in the eyes')
    c()
    print('\nthen he speaks:\nI\'m going to ask you a question, before you anwser think hard, \nbecause if you do and you are incorrect, you will spend the rest of eternity in hell.\nif you are correct you will have a chance of going back home.')
    c()
    print('''\nif * is an operation defined in R such that
\t1*2=4
\t2*2=8
\t3*2=14
\t4*2=24
\t5*2=42

what is a*b equal to:
Note that you should use * for multiplication 
** for exponential
+ for addition 
- for substraction
P.S do not put spaces in awnser ''')
    
    awns()



def dead(a):
    print(a)
    print('do you want to try again,press 1 if yes')
    awnser=input('>')
    if '1' in awnser:
        hf()
    else:
        exit(0)

def awns():
    awn=input('>')
    if 'a*b+b**a' in awn or 'b*a+b**a'in awn or 'b**a+a*b'in awn or 'b**a+b*a'in awn:
        print('correct unfortunately you will spend eternity in hell')
        dead('I\'m sorry but you\'ll get used to hell.')
    else:
        print('incorrect!! Try again!')
    awns()

def start():
    dim1()

def dim1():
    print ("A man is in love with the sounds that these 3 birds the bluejakes the owl and the eagle, and is bent on hearing the natural sounds of these birds whenever he wants.\nHe decides to go to a bird shop, but discovers that he has only enough money to buy only one bird.")
    c()
    print("He suddenly has a brainstorm and he buys one bird that will satisfy his desires. Wich bird does he buy?")
    x=input('>')
    if 'parrot'in x or 'parot'in x:
        print('correct')
        dim2()
    else:
        Dead('wrong awnser')

def dim2():
    print('What is the meaning of the word \'Tall\' in chinese')
    x=input('>')
    if 'same meaning' in x or 'tall'in x:
        print('correct bc the meaning of a word in one language is the same as the meaning of its translation in another language')
        print('As a reward you are given a crowbar')
        hf()
    else:
        dead('wrong awnser')

start()
