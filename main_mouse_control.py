# My LIBRARY
from tkinter import *
import numpy as np

window = Tk()
window.title("Pattern Selector")


rows = 25
columns = 35
size = 25
control = True # for control
list = [] # keeping track of changed boxes
i = 0       # generation counter

# Using convolution technique
kernel = [[1,1,1],
          [1,0,1],
          [1,1,1]]

cs = Canvas(window, width=columns*size, height=rows*size+40, bd=0, highlightthickness=0)
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
    ##print('painted all')

def clicked(event):
    global control, result, matrix
    if control:
        #print("in clicked")
        if cs.find_withtag(CURRENT):
            r, c = int(cs.gettags(CURRENT)[0]), int(cs.gettags(CURRENT)[1])
            result[r,c] = 1 if result[r,c] == 0 else 0
            list.append((r,c))

        matrix[1:rows+1, 1:columns+1] = result.copy()
        ##print(result)
        paint()

def paint():
    global list
    '''for (r,c) in list:                             # for j in range(len(list)):
        print(len(list))'''

    for (r,c) in tuple(list):
        if result[r,c] == 0:                       # (r,c) = list[j]
            cs.itemconfig(rects[r,c], fill="#ddd")
        else:
            cs.itemconfig(rects[r,c], fill="#777")
        list.remove((r,c))
        #print(j)
    #print("in paint = {}".format(list))

def do_it():
    global result, matrix, list, i, control
    control = False # CLICK EVENT DISABLED
    i += 1
    for r in range(rows):
        for c in range(columns):
            temp = int(np.sum(np.multiply(matrix[0+r:3+r,0+c:3+c], kernel)))
            ##print(np.multiply(matrix[0+r:3+r,0+c:3+c], kernel))
            if matrix[1+r,1+c] == 1: # It's ALIVE!!
                if temp == 2 or temp == 3:
                    state=1
                else:
                    state=0
            else:                    # It's DUDE!!
                if temp == 3:
                    state = 1
                else:
                    state = 0
            if state != matrix[1+r,1+c]:
                result[0+r,0+c] = state
                list.append((r,c))
    #print("in do_it = {}".format(list))
    matrix[1:rows+1, 1:columns+1] = result.copy()
    paint()
    #cs.pack()
    window.title("Pattern Selector | Generation = {}".format(i))
    cs.after(400, do_it)


cs.bind("<Button-1>", clicked)
#cs.after(5000, do_it)

Button(window, text ="START", command = do_it).pack()

paint_all()

window.mainloop()
