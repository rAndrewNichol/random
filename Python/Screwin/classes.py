# Classes and shit

class Point:
    pass

def printPoint(p):
    print('(' + str(p.x) +', ' + str(p.y) +')')

blank = Point()
blank.x = 3
blank.y = 4

printPoint(blank)

#Also:

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def printPoint(self):
        print('(' + str(self.x) +', ' + str(self.y) +')')
    #cooler option (this overrides str() and print())
    def __str__(self):
        return '(' + str(self.x) +', ' + str(self.y) +')'

    # operator overloader:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

blank = Point(3,4)
blank.printPoint()

class corner:
    def __init__(self, x, y):
        self.x, self.y = x, y

class rectangle:
    def __init__(self, width, height, corner):
        self.width, self.height, self.corner = width, height, corner
    def findCenter(self):
        x = self.corner.x + self.width/2
        y = self.corner.y - self.height/2
        p = Point(x,y)
        return p
    def growRect(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight
    def moveRect(self, dy, dx):
        self.corner.x += dx
        self.corner.y += dy


location = corner(4,5)

rect = rectangle(1,2,location)

rect.findCenter().printPoint()
rect.growRect(50,100)
rect.findCenter().printPoint()

#copying baby:
import copy
p1 = Point(3,4)
p2 = copy.copy(p1)
print(p1 is p2)
print(p1 == p2)
print(p1.x == p2.x and p1.y == p2.y)

print(p1)

#Now these are the same thing
print(p1 + p2)
print(p1.__add__(p2))