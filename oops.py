class student:
    name="hari"
a=student()

print(a.name)

#by using __init__
#class method(constructor)& self
class Subject:
    def __init__(self, chapter, hour):
        self.chapter = chapter
        self.hour = hour
    def full_info(self):
        return self.chapter,self.hour
           
english = Subject("chapter-2","cradit hour-8")
print(english.chapter)
print(english.hour)
print(english.full_info())

#Question 1: Basic Inheritance
#Create a class Animal with a method sound() that prints "Animal makes a sound".
#Create another class Dog that inherits from Animal and has a method bark() that prints "Dog barks".
#Create an object of Dog and call both methods.

class animal :
    def sound(self):
        print("animal make sound")
class dog(animal):
    def bark (self):
        print("dog bark")

d=dog()
d.sound()
d.bark()
