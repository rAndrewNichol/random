# Mouse
from Turtle import *


class Mouse(Turtle):
    def __init__(self, position, heading = 0, fill = brown, **style):
        Turtle.__init__(self, position, heading, fill = fill, **style)    
    
    #Scaling speed added for radio button options. Multiplies unit movement by speed and scales angle changes accordingly.
    speed = 1

    def getnextstate(self):
        """Rotate around statue 1m."""
        
        # If the mouse is caught, remove it from the arena and infinite loop "nom"
        if self.caught == True:
            print('NOM')
            return Vector(1000,1000), self.heading
        
        # Revolve around the statue by changing the angle one pixel each step.
        # According to scale, after 64 steps, the mouse will have revolved 1m (64 pixels)
        # around the statue.
        self.heading = self.heading - ( (180 * 1 * self.speed) / (self.radius * np.pi))
        self.angle = self.angle - ( (180 * 1 * self.speed) / (self.radius * np.pi))
        
        # Keep angles between 0 and 360 for simplicity and edgecases.
        if self.angle < 0: self.angle = 360 + self.angle
        
        return self.position + self.speed*unit(self.heading), self.heading

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*13,
                self.position - forward*7 - right*7,
                self.position - forward*4,
                self.position - forward*7 + right*7]