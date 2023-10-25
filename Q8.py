class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def intro(self):
        print("Hello",self.name)
        print("Age",self.age)
        print("gender:",self.gender)
       
class student(Person):
    def __init__(self,name,age,gender,course):
        super().__init__(name,age,gender)
        self.course=course
    def intro(self):
        super().intro()
        print("course:",self.course)
class teacher(Person):
    def __init__(self,name,age,gender,subject):
        super().__init__(name,age,gender)
        self.subject=subject
    def intro(self):
        super().intro()
        print("subject:",self.subject)    

S1=student("harsh",21,"male","Ai")
S1.intro()


               

