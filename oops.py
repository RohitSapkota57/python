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
