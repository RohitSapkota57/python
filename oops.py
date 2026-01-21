class student:
    name="hari"
a=student()

print(a.name)

#by using __init__
class Subject:
    def __init__(self, chapter, hour):
        self.chapter = chapter
        self.hour = hour
english = Subject(2,8)
print(english.chapter, english.hour)
