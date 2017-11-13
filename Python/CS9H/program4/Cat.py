# Cat 
from Turtle import *

class Cat(Turtle):
    def __init__(self, position, followee, heading = 0, fill = grey, **style):
        Turtle.__init__(self, position, heading, fill = fill, **style)
        self.followee = followee

    def getnextstate(self):
    #Rotate around statue 1.25m (in 64 steps).
        see = False

        # Normalize direction at each step 
        self.heading = self.angle - 90
        
        # The cat sees the mouse if (cat radius) * cos (cat angle – mouse angle) is at least 1.0.
        if ( (self.radius / 64) * cos( ((self.angle - self.followee.angle) * np.pi) / 180 ) ) >= 1.0:
            see = True

        # Once the cat reaches the same radius of the mouse, she stops there.
        if self.radius < 97: self.radius = 96

        # If the cat doesn't see the mouse or she has reached the same radius as the mouse.
        if see == False or self.radius == 96:

            # If the cat is ahead of the mouse around the statue and sees it
            if self.angle < self.followee.angle and see == True:
                # Catches mouse if mouse's next move crosses the cat's position
                #if ( self.followee.angle - ( (180 * 1) / (self.radius * np.pi)) ) -self.angle< self.angle:
                if abs((self.followee.angle - ( (180 * 1) / (self.radius * np.pi)) ) - self.angle) < 5:
                    self.followee.caught = True 
                # Stand still if she sees mouse coming toward her
                return self.position, self.heading

            # Continue to circle around the statue until cat sees mouse.    
            self.heading = self.heading - ( (180 * 1.25) / (self.radius * np.pi) )
            self.angle = self.angle - ( (180 * 1.25) / (self.radius * np.pi) )
            if self.angle < 0: self.angle = 360 + self.angle
            return self.position + unit(self.heading) * 1.25 , self.heading    

        # Move one meter toward statue if cat sees mouse.
        if see == True:
            # Point towards statue center
            self.heading = self.angle - 180
            self.radius = self.radius - 1
            return self.position + unit(self.heading), self.heading

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward*19,
                self.position - forward*10 - right*10,
                self.position - forward*6,
                self.position - forward*10 + right*10]
