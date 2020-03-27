from tkinter import *
import numpy as np
from time import sleep
from other_fns import *

window = Tk()
window.title("Pattern Selector")
#window.configure(background="black")
#window.geometry('800x610')

rows = 25
columns = 45
size = 25
sel = 1 # for selection mode

# Using convolution technique
kernel = [[1,1,1],
          [1,0,1],
          [1,1,1]]

cs = Canvas(window, width=columns*size, height=rows*size, bd=0, highlightthickness=0)


matrix = np.zeros(shape=(rows+2, columns+2), dtype=np.int32)
prev_result = np.zeros((rows,columns), dtype=np.int32)
result = np.zeros((rows,columns), dtype=np.int32)



def paint():

    print('painted')

def clicked(event):
    global sel, result, matrix
    if sel == 1:
        print("in clicked")
        if cs.find_withtag(CURRENT):
            r, c = int(cs.gettags(CURRENT)[0]), int(cs.gettags(CURRENT)[1])
            if result[r,c] == 0:
                result[r,c] = 1
                cs.itemconfig(CURRENT, fill="#aaa")
            else:
                result[r,c] = 0
                cs.itemconfig(CURRENT, fill="#ddd")

        matrix[1:rows+1, 1:columns+1] = result


    #paint(result)




        #cs.itemconfig(CURRENT, fill="#aaa")
        #cs.update_idletasks()

        # matrix setting 1 or 0


def do_it():
    global result, matrix
    print("in do_it")
        # playing the Game

    for r in range(rows):
        for c in range(columns):
            temp = int(np.sum(np.multiply(matrix[0+r:3+r,0+c:3+c], kernel)))
            result[0+r,0+c] = 1 if alive(temp) and  else 0

    matrix[1:rows+1, 1:columns+1] = result
    paint(result)

def go():
    global sel
    sel = 2
    print("sel=", sel)
    while(sel >= 2):
        cs.after(1000, do_it())
        cs.pack()
        window.title(("Pattern Selector - Generation = ",(sel - 1)))
        sel += 1


#cs.bind("<Key>", do_it)


'''
# EXECUTION BEGINS ##########################################################################################################
'''


paint(result)


cs.bind("<Button-1>", clicked)
cs.bind("<Double-1>", close)

cs.after(5000, go)

cs.pack()

window.mainloop()




'''
Label(window, bg='green', text="", relief=SUNKEN, width=2)\
    .grid(row=row, column=column)

Label(window, text="Presenting the Game of Life",
        fg="white", bg="black", font="none 12 bold")\
        .pack(padx=5, side=LEFT)

Label(window, text="Generation = 46",
        fg="white", bg="black", font="none 12 bold")\
        .pack(padx=5, side=RIGHT)'''
'''for r in range(rows):
    for c in range(columns):
        cs.create_rectangle(c*size,r*size,c*size+size,r*size+size,
                            outline="#cdcdcd", fill="#ddd" if c != 25 or r != 15 else "#aaa")'''





# Change title according to generation
