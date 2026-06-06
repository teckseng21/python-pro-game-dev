class Student():
    #properties
    name = "Tom"
    age = 10
    class_teacher = "Mr John"
    #constructor
    def __init__(self):
        print("Student object created")
    #method
    def display(self):
        print("Name:", self.name)
        print("Age:",self.age)
        print("Class Teacher:", self.class_teacher)
    def change_details(self):
        self.name=input("Enter the name:")
        self.age=input("Enter the age:")
        self.class_teacher=input("Enter the class teacher:")
#creating an object of the Student class
student1=Student()
student1.change_details()
student1.display()
student2=Student()
student2.change_details()
student2.display()