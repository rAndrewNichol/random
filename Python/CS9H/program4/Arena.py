from tkinter import *
from math import sin, cos, pi
from Vector import *
import os
from Color import *

os.chdir('C:/Users/Andrew/Documents/Coding/PythonFiles/CS9H/program4')
class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, statue, cat, mouse, width=400, height=400, **options):
        Frame.__init__(self, parent, **options)
        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        parent.title("Tom and Jerry Simulation 2.0")
        
        # Include simulation participants
        self.cat = cat
        self.mouse = mouse
        self.statue = statue

        #Reset button
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        self.turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        
        self.dragging = None

        # Time label:
        self.count = 0
        self.time = StringVar()
        self.time.set("Time: " + str( round(self.count / 64, 2) ))
        self.time_label = Label(self, textvariable = self.time)
        self.time_label.pack()

        # Cat radius label:
        self.cat_radius = StringVar()
        self.cat_radius.set("Cat Radius: " + str( round(self.cat.radius / 64, 2) ))
        self.cat_radius_label = Label(self, textvariable = self.cat_radius)
        self.cat_radius_label.pack()

        # Cat Angle Label:
        self.cat_angle = StringVar()
        self.cat_angle.set("Cat Angle: " + str( round(self.cat.angle,2) ))
        self.cat_angle_label = Label(self, textvariable = self.cat_angle)
        self.cat_angle_label.pack()

        # Mouse Angle Label:
        self.mouse_angle = StringVar()
        self.mouse_angle.set("Mouse Angle: " + str( round(self.mouse.angle, 2) ))
        self.mouse_angle_label = Label(self, textvariable = self.mouse_angle)
        self.mouse_angle_label.pack()

        #my picture LOL
        self.picofme = PhotoImage(file = "me.pgm")
            
        #About menu
        def about():
            filewin = Toplevel(self)
            filewin.title("About the UC Berkeley CS9H Turtle Arena")
            self.info = Label(filewin, text = "Andrew Nichol\n\
                UC Berkeley\n\
                Tom & Jerry Simulation 2.0")
            self.ok = Button(filewin, text = "Ok", command = filewin.destroy)
            self.pic = Label(filewin, image = self.picofme)
            self.pic.pack()
            self.info.pack()
            self.ok.pack()

        #Menubar
        self.menubar = Menu(self)
        #Add filemenu to menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = 'About...', command = about)
        # quit command already in Tk
        self.filemenu.add_command(label = 'Quit', command = parent.quit) 
        self.filemenu.add_separator()
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        parent.config(menu = self.menubar)

        #Radiobutton with default speed 1
        self.radiovalue = IntVar()
        self.radiovalue.set(1)
        Radiobutton(self, text= "Normal", variable = self.radiovalue, command = self.clickradio, value = 1).pack(anchor = W)
        Radiobutton(self, text= "Fast", variable = self.radiovalue, command = self.clickradio, value = 2).pack(anchor = W)
        Radiobutton(self, text= "Extreme", variable = self.radiovalue, command = self.clickradio, value = 3).pack(anchor = W)
        
    def clickradio(self):
        # Mouse speed becomes 2x if "Fast" is selected and 3x if "Extreme" is selected
        self.mouse.speed = self.radiovalue.get()

    # reset function returns all of cat and mouse values to starting positions, which are defined in the simulator
    # also reset's mouse status to 'not caught'    
    def reset(self):
        self.cat.position, self.cat.angle, self.cat.radius, self.cat.heading = self.cat.start_pos 
        self.mouse.position, self.mouse.angle, self.mouse.radius, self.mouse.heading = self.mouse.start_pos
        self.mouse.caught = False
    
    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        # Change cat color to black if mouse over cat during motion
        if (Vector(event.x, event.y) - self.cat.position).length() < 12: 
            self.cat.style['fill'] = Color(0,0,0) 
        else: self.cat.style['fill'] = grey
        
        drag = Vector(event.x, event.y)
        #if drag.x - self.cat.position.x <= 50: self.cat.fill = black
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            self.update(self.dragging)

    def release(self, event):
        # return cat heading to normal
        self.cat.heading = self.cat.angle - 90 
        #self.cat.style['fill'] = grey
        self.dragging = None


    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)
        if self.dragging == self.cat:
            # Updating values during drag
            self.cat.position = self.dragging.position
            self.cat.angle = (self.cat.position - self.statue.position).direction()
            self.cat.radius = (self.cat.position - self.statue.position).length()
            self.cat_angle.set("Cat Angle: " + str( round(self.cat.angle,2) ))
            self.cat_radius.set("Cat Radius: " + str( round(self.cat.radius / 64, 2) ))            
            # Make cat face toward center while being moved.
            self.cat.heading = self.cat.angle - 180 

    def add(self, turtle):
        """Add a new turtle to this arena."""
        self.turtles.append(turtle)
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        nextstates = {}

        # Time update
        if self.mouse.caught != True: self.count += 1
        self.time.set('Time: ' + str( round(self.count / 64, 2) ))

        # Cat Radius update
        self.cat_radius.set("Cat Radius: " + str( round(self.cat.radius / 64, 2) ))

        # Cat Angle Update
        self.cat_angle.set("Cat Angle: " + str( round(self.cat.angle, 2) ))
        
        # Mouse Angle Update
        self.mouse_angle.set("Mouse Angle: " + str( round(self.mouse.angle, 2) ))
        
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
        if stop:
            self.running = 0



    def run(self):
        """Start the turtles running."""
        self.running = 1
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)
        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0



    # def on_enter(self):
    #     pass

    # def on_leave(self):
    #     pass

    # self.cat.bind('<Enter>', self.on_enter)
    # self.cat.bind('<Leave>', self.on_leave)