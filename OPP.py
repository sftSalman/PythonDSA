class Dog:
    species = 'mamaml'
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(self.name ,'can barks')

tommy = Dog('Tommy')
print(tommy.name,tommy.species,tommy.bark())