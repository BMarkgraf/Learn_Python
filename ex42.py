# Animal is-a object (yes, sort of confusing) look at the extra credit line
class Animal(object):
    pass

# Dog is-a class of object Animal
class Dog(Animal):
    def __init__(self, name):
        # ??
        self.name = name

# Cat is-a class of object Animal
class Cat(Animal):
    def __init__(self, name):
        # ??
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self,name):
        # ??
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is a class of object Person
class Employee(Person):
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is a class of object Fish
class Salmon(Fish):
    pass

# Halibut is a class of object Fish
class Halibut(Fish):
    pass

# rover is-a object Dog
rover = Dog("Rover")

# satan is-a object Cat
satan = Cat("Satan")

# mary is-a object Person
mary = Person("Mary")

# frank is-a object Employee that is-a class Person
frank = Employee("Frank", 120000)

# franks pet has-a name of rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut that is-a Fish
harry = Halibut()
