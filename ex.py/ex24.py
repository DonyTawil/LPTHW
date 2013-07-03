from sys import argv
(script, start_point)=argv
print ("Let's practice everything.")
print ('You\' d need to know \' bout escapes with that \\ to do \n newlines and \t tabs.') 

poem = """
\tthe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print (poem)
print("--------------")

five = 10 - 2 + 3 - 6
print ("this should be five: %d"%five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return (jelly_beans, jars, crates)

int(start_point)
print(int(start_point))
beans, jars, crates = secret_formula(int(start_point))

print ("With a starting point of: %d"%int(start_point))
print ("we'd have %d beans, %d jars, and %d crates."%(beans, jars, crates))

start_point = int(start_point) / 10

print ("we can also do that this way:")
print ("with this much for starting point: %d"%start_point)
print (" we'd have %d beans, %d jars, and %d crates."%secret_formula(int(start_point)))
