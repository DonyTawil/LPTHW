cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY']='New York'
cities['OR']= 'portland'

print(cities['NY'])
print(type(cities))
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities['h'] = find_city

while True:
    print("State? (Enter to quit)")
    state = input("> ")

    if not state:
        break

    city_found = cities['h'](cities, state)
    print(city_found) 

print(cities.items())

for h in cities:
    print(cities[h])

print(1 in cities)
print('CA'in cities)
print('San Francisco'in cities)
