from tkinter import *
from Arena import Arena
from Turtle import Turtle
from Vector import *
from Statue import *
from random import *
from Cat import *
from Mouse import *
import numpy as np

# Scale for this arena simulation taken from the class variable Turtle.scale
scale = Turtle.scale

# Initialize tkinter object
tk = Tk()

# Initialize and add statue. Picks a random position which is limited to 
# positions closer to the center of the arena
statue = Statue(Vector(randint(150,250), randint(150,250)),0)

# Place the mouse 1.5 m from the center of the statue at a random angle
tom_pos = (unit(0)*scale*1.5).rotate(randint(0,360)) + statue.position
tom = Mouse(tom_pos)
# Get angle from statue center to mouse position using vector arithmetic
tom.angle = (tom.position - statue.position).direction()
# Point in clockwise direction
tom.heading = tom.angle - 90 
# Mouse is 1.5m from center of statue
tom.radius = 1.5 * scale
# Initialize mouse as not-caught 
tom.caught = False

tom.start_pos = tom_pos, tom.angle, tom.radius, tom.heading

# Place the cat at a random position in the arena,  avoiding the zone 
# where the statue and mouse were placed.
jerry_pos = Vector(choice([randint(20, statue.position.x - scale*1.5), 
	                       randint(statue.position.x + scale*1.5, 380)]),
	             choice([randint(20, statue.position.y - scale*1.5), 
	             	     randint(statue.position.y + scale*1.5, 380)]))

jerry = Cat(jerry_pos, followee = tom)
jerry.angle = (jerry.position - statue.position).direction()
jerry.radius = (jerry.position - statue.position).length()
jerry.heading = jerry.angle - 90
jerry.start_pos = jerry_pos, jerry.angle, jerry.radius, jerry.heading

arena = Arena(tk, statue, jerry, tom) 
arena.pack()


arena.add(tom)
arena.add(jerry)
arena.add(statue)


tk.mainloop()