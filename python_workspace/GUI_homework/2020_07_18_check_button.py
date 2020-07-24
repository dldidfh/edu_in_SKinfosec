import tkinter

windo = tkinter.Tk()
frame = tkinter.Frame(windo)
frame.pack()

red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()

for (name,var) in (('R',red),('G',green),('B',blue)):
    check = tkinter.Checkbutton(frame,text=name,variable=var)
    check.pack(side='left')
def recolor(widget,r,g,b):
    color = '#'
    for var in (r,g,b):
        #color += 'FF' if var.get() else '00'
        if var.get() :
            color += 'FF'
        else:
            color += '00'
    widget.config(bg=color)

label = tkinter.Label(frame, text='[]')
button = tkinter.Button(frame,text='update', command=lambda:recolor(label, red, green, blue))
button.pack()
label.pack()
windo.mainloop()
