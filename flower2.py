from turtle import *

def flower():
    speed(0)
    for i in range(200):  # Decrease the number of loops
        circle(150 - i * 0.5, 60)  # Modify the radius and angle
        left(120)  # Change the rotation angle
        circle(150 - i * 0.5, 60)
        left(15)  # Adjust the main rotation angle
flower()
done()
