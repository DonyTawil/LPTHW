##Animal is-a object
class Animal(object):
    kids=0

    def __init__(self):
        self.kids=kids

    def mate(self):
        self.kids+=1

##Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##has-a name
        self.name = name    


##is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##has-a name
        self.name = name
      

##is-a object
class Person(object):

    def __init__(self, name):
        ##has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

## is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##has-a name
        super(Employee, self).__init__(name)
        ##has-a salary
        self.salary = salary

##is-a object
class Fish(object):
    pass

##is-a fish
class Salmon(Fish):
    pass

##is-a Fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")
rover.mate()
print(rover.kids)

##satan is-a Cat
satan = Cat("Satan")
print("this is satan's kids",satan.kids)
##Mary is-a person
mary = Person("Mary")

##Mary has-a pet is-a cat has-a name 
mary.pet = satan

##is-a employee
frank = Employee("Frank",120000)

##has-a pet is-a dog(Fran.pet is now an instance OMG)
frank.pet = rover

##flipper is-a fish
flipper =Fish()

##is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()


                                      
