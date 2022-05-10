import turtle
import random
from PIL import Image

# instantiating turtle object named 'bob'
bob = turtle.Turtle()

# setting the speed of drawing
bob.speed(1)

# setting the color mode (either 1 or 255)
turtle.colormode(255)

# opening text file with mobile phone dimensions
with open('dimensions.txt', 'r', encoding='utf-8') as file:
    dimensions = file.readlines()

    # moving the cursor to the left to start drawing vertically
    bob.left(90)

    # the main loop
    for dimension in dimensions:

        # choosing random rgb color components
        r, g, b = (random.randint(0, 255) for _ in range(3))
        bob.color((r, g, b))

        # cleaning text file data to be in raw numeric float format
        dimension = dimension.replace(' mm', '').replace('\n', '')
        h, w, d = dimension.split(' x ')
        h, w, d = float(h), float(w), float(d)

        # drawing the phone outline from the front
        bob.forward(round(h))
        bob.left(90)
        bob.forward(round(w))
        bob.left(90)
        bob.forward(round(h))
        bob.left(90)
        bob.forward(round(w))

        # moving the cursor to the side
        bob.penup()
        bob.forward(80)
        bob.left(90)
        bob.pendown()

        # drawing the phone outline view from the side
        bob.forward(round(h))
        bob.left(90)
        bob.forward(round(d))
        bob.left(90)
        bob.forward(round(h))
        bob.left(90)
        bob.forward(round(d))


        # moving the cursor to the side and further down
        bob.penup()
        bob.left(90)
        bob.left(90)
        bob.forward(80)
        bob.left(90)
        bob.forward(80)
        bob.right(90)
        bob.pendown()

        # drawing the phone outline for top view
        bob.forward(round(w))
        bob.left(90)
        bob.forward(round(d))
        bob.left(90)
        bob.forward(round(w))
        bob.left(90)
        bob.forward(round(d))

        # going back to the start position for the next iteration
        bob.penup()
        bob.forward(80)
        bob.pendown()

# saving file as .eps
ts = turtle.getscreen()
eps_file = 'phones.eps'
ts.getcanvas().postscript(file=eps_file)

# converting .eps to .png
im = Image.open(eps_file)
fig = im.convert('RGBA')
image_png = 'phones.png'
fig.save(image_png, lossless= True)
