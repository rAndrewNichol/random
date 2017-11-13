# Statue

from Turtle import *

class Statue(Turtle):
    def __init__(self, position, heading, fill = firebrick, **style):
        Turtle.__init__(self, position, heading, fill = fill, **style)

    # Set 360 vertices for the outside shape of the statue. Technically, the statue
    # is a 360-sided polygon. For all intents and purposes, it appears circular.    
    def getshape(self):
        zero = unit(0)
        points = []
        # Builds a list of angles between 1 and 360.
        for i in range(360):
            points.append(self.position + self.scale * zero.rotate(1 * i))
        return points



