from tkinter import *
import math
import random

from definitions import *

root = Tk()
root.geometry("800x800+30+30")
after_id = None
stations = []
trains = []
stations_dict = {"Комсомольская":3, "Курская":6, "Таганская":8, "Павелецкая":11, "Добрынинская": 13, "Октябрьская":14, "Парк культуры":17,
                 "Киевская":20, "Краснопресненская":22, "Белорусская":25, "Новослободская":27, "Проспект Мира":0}

def start_modelling():
    global after_id
    global trains
    for i in range(len(trains)):
        trains[i].hide()
        trains[i].move()
        trains[i].show()
    after_id = root.after(1000,start_modelling)

def stop_modelling():
    if after_id != None:
        root.after_cancel(after_id)
    for t in trains:
        st.show()


panelFrame = Frame(root, relief=RAISED, borderwidth=1)
panelFrame.pack(fill=BOTH, expand=False)

startBtn = Button(panelFrame, text="Старт", width=10, height=1, bg="White", fg = "black", command=start_modelling)
stopBtn = Button(panelFrame, text="Стоп", width=10, height=1, bg="White", fg = "black", command=stop_modelling)
startBtn.pack(side=LEFT, pady=3)
stopBtn.pack(side=RIGHT, pady=3)

c = Canvas (root, width=700, height=700, bg='white')
c.pack(pady=10)

ring1 = Ring (c, _radius = 300, _width = 3)
ring2 = Ring (c, _radius = 290, _width = 3, _rotation = 1)
ring3 = Ring (c, _radius = 295, _rotation = 1)
ring1.show()
ring2.show()

for i in stations_dict.keys():
    st = Station(c, ring3, _start_time = stations_dict[i]);
    stations.append(st)
    st.show()

#Читаем информацию из файла и создаем поезда соответствующим образом


file=open('metro.txt')
for line in file:
    line = line.split(' ')
    start_pos=stations_dict[line[1]]
    if line[2]=='1':
        ring=ring1
    else:
        ring=ring2
    vagon=int(line[3])
    speed=int(line[4])
    t = Train(c, ring, start_pos, vagon, _color="Blue", _speed = speed)
    trains.append(t)
    t.show()

root.mainloop()
