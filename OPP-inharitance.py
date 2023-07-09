
class Person:
    def __init__(self,name ,id ):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print('This is {}'.format(self.name))
        print("id is {}".format(self.id))


class Emp(Person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name,id)
    def details(self):
        print('name is {}'.format(self.name))
        print('post{}'.format(self.post))



a = Emp('salman',123,2000,'clark')
print(a.name, a.id, a.post,a.salary)