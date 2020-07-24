import tkinter
import tkinter.filedialog as dialog
class main_open:

    def __init__(self, window1):

        self.window1 = window1
        self.frame = tkinter.Frame(window1)
        self.frame.pack()
        self.text = tkinter.Text(window1)
        self.text.pack()

        menubar = tkinter.Menu(window1)
        filemenu = tkinter.Menu(menubar)
        filemenu.add_command(label='Save', command=self.save)
        filemenu.add_command(label='Quit', command=self.quit)

        menubar.add_cascade(label='File',menu=filemenu)
        window1.config(menu=menubar)

    def save(self):
        data = self.text.get('0.0', tkinter.END)
        filename = dialog.asksaveasfilename(parent=self.window1, filetypes=[('Text','*.txt')], title='Save as...')
        writer = open(filename,'w')
        writer.write(data)
        writer.close()

    def quit(self):
        self.window1.destroy()



if __name__ == '__main__':
    window = tkinter.Tk()
    main = main_open(window)
    window.mainloop()