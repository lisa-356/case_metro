import math
import tkinter

class ModelObject(object):
    def __init__ (self, _canvas):
        self.canvas = _canvas
        self.id = None

    def show(self):
        self.draw();

    def hide(self):
        if self.id != None:
            self.canvas.delete(self.id)


class Ring(ModelObject):
    def __init__ (self, _canvas, _radius = 300, _color = "black", _start_x = 350, _start_y = 350, _width=4, _rotation = 0):
        ModelObject.__init__(self, _canvas)
        self.radius = _radius;
        self.color = _color;
        self.start_x = _start_x
        self.start_y = _start_y
        self.width   = _width
        self.rotation = _rotation

    def draw(self):
        self.canvas.create_oval (self.start_x - self.radius, self.start_y - self.radius,
                                 self.start_x + self.radius,  self.start_y + self.radius,
                                 outline=self.color, width=self.width)

class Station(ModelObject):
    def __init__ (self, _canvas, _ring, _start_time = 0, _radius = 10, _color = "red", _width = 4, _fill="red"):
        ModelObject.__init__(self, _canvas)
        self.ring = _ring;
        self.start_time = _start_time
        self.radius = _radius
        self.color = _color
        self.width = _width
        self.fill = _fill

    def draw(self):
        if (self.ring.rotation > 0):
            time_position = math.radians(90 - self.start_time * 12)
        else:
            time_position = math.radians(90 + self.start_time * 12)
        start_x = self.ring.start_x + self.ring.radius * math.cos(time_position)
        start_y = self.ring.start_y - self.ring.radius * math.sin(time_position)
        
        self.id = self.canvas.create_oval (start_x - self.radius, start_y - self.radius,
                                           start_x + self.radius, start_y + self.radius,
                                           outline=self.color, width=self.width, fill=self.fill)

class Train(ModelObject):
    def __init__ (self, _canvas, _ring, _start_time = 0, _carriage = 1, _speed = 0.5, _color = "red", _width = 8, _fill="red"):
        ModelObject.__init__(self, _canvas)
        self.ring = _ring;
        self.start_time = _start_time
        self.carriage = _carriage
        self.color = _color
        self.width = _width
        self.fill = _fill
        self.speed = _speed
        self.arc_len = _carriage*2*180/(_ring.radius * math.pi)

    def draw(self):
        if (self.ring.rotation > 0):
            start_time_position = 90 - self.start_time * 12
        else:
            start_time_position = 90 + self.start_time * 12
        self.id = self.canvas.create_arc (self.ring.start_x - self.ring.radius, self.ring.start_y - self.ring.radius,
                                          self.ring.start_x + self.ring.radius, self.ring.start_y + self.ring.radius,
                                          start = start_time_position, extent = self.arc_len, style=tkinter.ARC,  outline=self.color, width=self.width)

    def move(self):
#Нужно сделать расчет перемещения исходя из скорости. Не забываем, что паровоз имеет свойство "стоять" на станции!!!
        self.start_time += self.speed
        if (self.start_time > 30):
            self.start_time -= 30
        
