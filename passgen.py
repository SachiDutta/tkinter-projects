import random
import pyperclip 
from tkinter import *
from tkinter.ttk import *
import string 

root=Tk()
root.geometry('640x480')
root.configure(background='white')
root.title('Password Generator')
root.resizable(False,False)

label1=Label(root,text='GENERATE YOUR PASSWORD :',font='Georgia 17 italic')
label1.pack(pady=20)

label2=Label(root,text='Input password length :', font='Geogia 15 ',justify='left')
label2.configure(foreground='black',background='white')
label2.place(x=10,y=90)
label2_len= IntVar()
length=Spinbox(root,from_ = 4, to_ = 12,textvariable=label2_len, width = 28, font='Georgia 15 bold').place(x=20,y=130)

output=StringVar()
combinations=string.ascii_letters+string.digits+string.punctuation


def randPassGen():
        password= ''
        for y in range(label2_len.get()):
            characters=random.choice(combinations)
            password=password +random.choice(characters)

        output.set(password)



 
def copyPass():
    pyperclip.copy(output.get())
    


b1=Button(root, command = randPassGen, text = "Generate Password" )
b1.pack(padx=20, pady=20)

b1.pack(padx=20,pady=120)

label3=Label(root,text='Generated Password : ',font='Georgia 15')
label3.configure(foreground='black',background='white')
label3.place(x=10,y=230)
Entry(root , textvariable = output, width = 24).place(x=20,y=271)


b2=Button(root, text = ':: Copy the password to Clipboard', command = copyPass).pack()


root.mainloop()
 

 









