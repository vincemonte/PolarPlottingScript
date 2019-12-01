import turtle
import math
import re

'''
For now it will only work with multiples of theta and
function constants in base10; merely lazy-parsing
'''

#we can always change this to make the screen larger
class Graph:
    def __init__(self):
        self.screen_radius = 300
        self.font_size = 8
        self.font = ("Arial", self.font_size, "bold")
        self.width = self.screen_radius * 2 + 100
        self.height = self.screen_radius * 2 + 100
        self.degree_label_screen_radius = self.screen_radius + 16
        turtle.screensize(canvwidth=self.width, canvheight=self.height)
        turtle.setup(width=self.width + 40, height=self.height + 40)
        turtle.speed(0) #0 speed means no drawing :D
        turtle.hideturtle()
        self.draw_axes()
        self.draw_radialaxes()
        #self.draw_concentric_circles()
        self.plot_turtle = turtle.Turtle()
        turtle.showturtle()
        turtle.delay(25)
    '''
    def parseInString(self, in_string):
        try:
            self.function_constant = float(in_string[0])
        except ValueError:
            self.function_constant = 1
            self.trig_name = in_string[0:3]
            self.multiple_of_theta = in_string[3]
        else:
            self.trig_name = in_string[1:4]
            self.multiple_of_theta = in_string[4]
        try:
            self.multiple_of_theta = float(self.multiple_of_theta)
        except ValueError:
            self.multiple_of_theta = 1
    '''


    def draw_axes(self):
        turtle.pencolor((1, 0, 0))
        turtle.pensize(1.75)
        for degree in range(0, 360, 90):
            radians = math.radians(degree)
            turtle.pendown()
            turtle.goto(math.cos(radians) * self.screen_radius,
                        math.sin(radians) * self.screen_radius)
            turtle.penup()
            turtle.goto(math.cos(radians) * self.degree_label_screen_radius,
                        math.sin(radians) * self.degree_label_screen_radius)
            turtle.goto(turtle.position()[0], turtle.position()[1] - self.font_size)
            turtle.pendown()
            turtle.write(str(degree) + u'\u00B0', align='left', font=self.font)
            turtle.penup()
            turtle.home()
        #now add for loop to tick off the x and y's
        turtle.pensize(1.5)
        for degree in range(0, 360, 90):
            radians = math.radians(degree)
            #loop will be based off pixel sizes, going in steps of 60 gives me 4 markers (5 including 0)
            for distance in range(0, self.screen_radius, 60):
                turtle.penup()
                turtle.goto(math.cos(radians) * distance,
                            math.sin(radians) * distance)
                turtle.pendown()
                if degree == 0 or degree == 180:
                    turtle.left(90)
                    turtle.forward(15)
                    turtle.left(180)
                    turtle.forward(30)
                    turtle.penup()
                    turtle.home()
                else:
                    turtle.forward(15)
                    turtle.left(180)
                    turtle.forward(30)
                    turtle.penup()
                    turtle.home()

    def draw_radialaxes(self):
        turtle.pencolor('black')
        turtle.pensize(1)
        for degree in range(0, 360, 15):
            radians = math.radians(degree)
            if degree % 90 != 0:
                turtle.pendown()
                turtle.goto(math.cos(radians) * self.screen_radius,
                            math.sin(radians) * self.screen_radius)
                turtle.penup()
                turtle.goto(math.cos(radians) * self.degree_label_screen_radius,
                            math.sin(radians) * self.degree_label_screen_radius)
                turtle.goto(turtle.position()[0], turtle.position()[1] - self.font_size)
                turtle.pendown()
                turtle.write(str(degree) + u'\u00B0', align='left', font=self.font)
                turtle.penup()
                turtle.home()
    #fix this!
    def draw_concentric_circles(self):
        turtle.speed(0)
        turtle.pencolor('grey')
        turtle.pensize(.7)
        for radius in range(0, 360):
            turtle.pendown()

            turtle.penup()
            turtle.home()

    '''
    - must take parameter for multiple of theta
    - must take parameter for trig Function
    - must take parameter for constant
    - distance (r) is represented in terms of theta
        o e.g. r(t) = cos(2t)
    - pass in trig_name to decide eventually
    '''
    def plot(self, in_string):
        #multiply by 100 to adjust to the screensize based values
        self.plot_turtle.clear()
        self.plot_turtle.home()
        self.plot_turtle.penup()
        self.plot_turtle.pencolor('blue')
        self.plot_turtle.pensize(2.5)
        additive, function_constant, trig_function, multiple_of_theta = self.parse_input_str(in_string)
        radius_of_obj = function_constant * 60
        additive *= 60
        for degree in range(0, 360 + 1):
            radians = math.radians(degree)
            #change this simple function
            r = additive + (radius_of_obj * trig_function(radians * multiple_of_theta))
            x = r * math.cos(radians)
            y = r * math.sin(radians)
            self.plot_turtle.goto(x, y)
            self.plot_turtle.pendown()
        self.plot_turtle.penup()

    '''
    -return 1 if the string is empty
    '''
    def decide_trig_function(self, function_string):
        if function_string.lower() == 'cos':
            return math.cos
        elif function_string.lower() == 'sin':
            return math.sin
        elif function_string.lower() == 'tan':
            return math.tan
    '''
    Group 1: function_constant
    Group 2: trig_function
    Group 3: coefficient_of_theta

    -parse for an additive, for sqrt
    '''
    def parse_input_str(self, in_string):
        pattern = re.compile(r'(\d\s?\+\s?)?(\d)?(\w+)(\(\d\w+\))?')
        matches = pattern.finditer(in_string)
        match = next(matches)
        additive = match.group(1)
        function_constant = match.group(2)
        trig_function = match.group(3)
        coefficient_of_theta = match.group(4)
        if additive is None:
            additive = 0
        else:
            additive = int(additive[0])
        if function_constant is None:
            function_constant = 1
        else:
            function_constant = int(function_constant)
        if coefficient_of_theta is None:
            coefficient_of_theta = 1
        else:
            coefficient_of_theta = int(coefficient_of_theta[1])
        return additive, function_constant, self.decide_trig_function(trig_function), coefficient_of_theta



#4-leafed rose (clover)
#graph.plot('2sin(2t)')
in_string = input('Type function now. \n')
graph = Graph()
graph.plot(in_string)


turtle.exitonclick()

'''
Notes
=====
- turtle starts at (0, 0)
- turtle lib has the ability to slow down drawing
    o slow down drawing for the graphing
- distance in turtle is measured in pixels
- I want to draw the plots around r distances and mark them
  on the x and y axes
- PyQt5:
    o command to convert .ui into .py: pyuic5 filename.ui > filename.py
'''

'''
Notes on origin plotting script
===============================
- Drawing the axes took in a screen_radius and based the screen and coords to draw radial axes to based on that
    o I think I want to have a static screen_radius
- To plot different graphs, he is calling a different specified function
  to be able to the position the turtle should go to
    o Position returned as a dictionary

'''

'''
Checklist
=========
- Draw concentric circles (radii range: 0 (pole) - 9)
    o Draw around an x and y axis, label the distances so that radii can be distinguished
- Function to take in polar equation (tell user what symbol to use)
    o Implement GUI (I want this as easy as possible for Servas)
        + Change the styles in the actual python code
- learn proper parsing to handle more complex args and make the ui nicer

~ Hook up graphic to OpenGL and insert into gui?
'''
