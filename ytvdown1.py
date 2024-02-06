from tkinter import *
import time
from pytube import YouTube



def animate_label(text, label, cursor,delay=14):
    for i in range(len(text) + 1):
        partial_text = text[:i]
        label.config(text=partial_text + cursor)
        root.update()
        time.sleep(delay / 1000.0)
        

# Create-Display Window
root = Tk()
root.title('YouTube Video Downloader')
root.configure(bg='black')
root.geometry('590x420')
root.resizable(0, 0)

label1=Label(root,text='>',font='Helvetica 14',bg='black',fg='white')
label1.place(x=10,y=15)

label2_text = ' Download any YouTube video of your choice! '
cursor_char = '|'

label2 = Label(root, text='', bg='black', fg='white', font=('Times New Roman', 15,'italic underline'))
label2.place(x=10,y=50)

# Call the function to animate the label text with cursor
animate_label(label2_text, label2, cursor_char)

link = StringVar()
label3=Label(root, text = 'Paste the URL here:',bg='pale violet red', font = 'Helvetica 15 bold').place(x= 20, y = 100)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 20, y = 140)



def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Your video has been successfully downloaded!', font = 'Helvetica 15').place(x= 100 , y = 290)  
Button(root,text = 'DOWNLOAD', font = 'Helvetica' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=230 ,y = 210)



root.mainloop()
