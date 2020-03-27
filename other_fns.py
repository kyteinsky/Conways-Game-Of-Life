# My LIBRARY
from tkinter import *
import numpy as np

window = Tk()
window.title("Pattern Selector")


rows = 25
columns = 45
size = 25
control = True # for control && generation counter
list = [] # keeping track of changed boxes

# Using convolution technique
kernel = [[1,1,1],
          [1,0,1],
          [1,1,1]]

cs = Canvas(window, width=columns*size, height=rows*size, bd=0, highlightthickness=0)
cs.pack()


matrix = np.zeros(shape=(rows+2, columns+2), dtype=np.int32)
result = np.zeros((rows,columns), dtype=np.int32)
rects = np.zeros((rows,columns), dtype=np.int32)

def paint_all():
    for r in range(rows):
        for c in range(columns):
            rects[r,c] = cs.create_rectangle(c*size,r*size,c*size+size,r*size+size,
                                            outline="#cdcdcd",fill="#ddd",
                                            tags=str(r)+" "+str(c))
    print('painted all')

def clicked(event):
    global control, result, matrix
    if control:
        print("in clicked")
        if cs.find_withtag(CURRENT):
            r, c = int(cs.gettags(CURRENT)[0]), int(cs.gettags(CURRENT)[1])
            result[r,c] = 1 if result[r,c] is 0 else 0
            list.append((r,c))

        matrix[1:rows+1, 1:columns+1] = result.copy()
        paint()

def paint():
    for (r,c) in list:
        cs.itemconfig(rects[r,c], fill="#ddd" if result[r,c] is 0 else "#777")
        list.remove((r,c))
    print('painted')

def do_it():
    control = False # CLICK EVENT DISABLED
    while(True):
        print('in do_it')
        



cs.bind("<Button-1>", clicked)
paint_all()

window.mainloop()
