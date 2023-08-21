# Event Deriven Programming is a programming paradigm that introduces events while developing the SW APP.
#Events are the occurrence of activities that will happen as a result of some user actions like:
# mouse-move or button-click.

# The advantages of using event-driven programming paradigm are listed below: 
# •Easy to develop systems even for beginners 
# •Provide object-oriented features like code reuse, use of classes, etc. 
# •Flexibility to choose programming tools 
# •Provide Graphical Interfaces for designing and creating applications. 
# •Simple programming constructs. 
# •The interactive application is generated.


import sys
import tkinter as tr
from turtle import width

def main():
    root = tr.Tk()
    root.title("Event Deriven Programming")
    root.resizable(width = True, height = True)

    def quit():
        root.destroy()


    bar = tr.Menu(root)
    fileMenue = tr.Menu(bar, tearoff=0)
    fileMenue.add_command(label="Exit", command=quit)
    bar.add_cascade(label="File", menu=fileMenue)
    root.config(menu=bar)   
    tr.mainloop()



    if __name__ == '__main__':
        main()