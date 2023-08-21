# classmethod() is an inbuilt function in Python, which returns a class method for agiven function.
# We use @classmethod decorator in Python to create a class method.
# The classmethod() methods are bound to a class rather than an object.
# A class method takes cls as the first parameter and can access or modify the class state.


from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name is {self.name} , Age is {self.age} "

    @classmethod
    def initFromBirthYear(cls, name, birthYear, extra):
        return cls(name, date.today().year - birthYear, extra)

class Woman(Person):
    gender = 'Female'
    num_of_Women = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.num_of_Women +=1

    def display(self):
        string = super().display()
        return string + f" , Hair is {self.hair} and Gender is {self.gender} "


womam = Woman("Nawal", 22, "stright")
print(Woman.display(womam))

woman2 = Woman.initFromBirthYear("Manar", 2003, "curly")
print(Woman.display(woman2))