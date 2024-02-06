from tkinter import * 
from playsound import playsound

def click(event):    #click event handler that handles all button clicks
    global scvalue   #global variable to store the current value displayed on the screen
    text = event.widget.cget('text')  #To get the text of the button that was clicked
    if text == "=":
        try:
            value= eval(scvalue.get()) #eval function is used to evaluate the arithmetic expression entered
        except Exception as e: #except block catches the error 
            print(e)
            value="Error"
        scvalue.set(value)
        screen.update()  # creates a new instance of the Tkinter class to create the main window for the calculator
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.icursor(END)
        screen.update()
    playsound('C:\\Users\\dutta\\Downloads\\mixkit-mouse-click-close-1113.wav') #plays click sound
        
root=Tk()  #creates a new instance of the Tkinter class to create the main window for the calculator
root.geometry('645x940') #sets the size of the main window, here 645 is width and 940 is length
root.title("Basic Calculator") #displays the title at the top of the main window 
root.configure(bg='#333333') #sets background colour of the main window

scvalue = StringVar()
scvalue.set("") #scvalue.set is used to set the value of StringVar()
screen=Entry(root,textvar=scvalue, font='Georgia 32 italic', bd=5,bg='#e6e6e6', relief=GROOVE)
screen.pack(fill=X, ipadx=8, pady=10, padx=10) #screen.pack is used to display the widget on the window

# Creates a new Frame widget 'f' with a grey bg, a border width of 5,
# a relief style (determines the appearance of the border of widget ) = 'groove'
f=Frame(root, bg="grey",bd=5,relief=GROOVE) 
#Creates a new Button widget 'b' with a text, a width of 28 pixels, a height of 18 pixels, and a font of 'helvetica 35 bold'
b=Button(f, text="9", padx=28,pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5) #Packs the Button widget 'b' onto the left side of the Frame widget 'f'
b.bind("<Button-1>",click) #Binds a left mouse click event to the Button widget 'b'

b=Button(f, text='8', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='7', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack() #to display the frame containing the buttons on the main window

f = Frame(root, bg='grey',bd=5,relief=GROOVE)
b=Button(f, text='6', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='5', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='4', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg='grey',bd=5,relief=GROOVE)
b=Button(f, text='3', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='2', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='1', padx=28, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg='grey',bd=4,relief=GROOVE)
b=Button(f, text='0', padx=31, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='-', padx=31, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='*', padx=31, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg='grey',bd=4,relief=GROOVE)
b=Button(f, text='/', padx=30, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='+', padx=30, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f, text='=', padx=30, pady=18, font="helvetica 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
