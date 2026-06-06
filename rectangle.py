import pygame

screen=pygame.display.set_mode((400, 300))

class Rectangle():
    #properties
    length = 0
    breadth = 0
    color = "red"
    #constructor
    def __init__(self):
        print("Rectangle object created")
    #method
    def display(self):
        print("Length:", self.length)
        print("Breadth:",self.breadth)
        print("Color:", self.color)
    def change_details(self):
        self.length=input("Enter the length:")
        self.breadth=input("Enter the breadth:")
        self.color=input("Enter the color:")
    def draw(self):
        self.draw_rectangle=pygame.draw.rect(screen,self.color, (self.length, self.breadth) )
#creating an object of the Rectangle class
rectangle1=Rectangle()
rectangle1.change_details()
rectangle1.draw()
rectangle1.display()
rectangle2=Rectangle()
rectangle2.change_details()
rectangle2.display()
