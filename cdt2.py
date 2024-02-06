from tkinter import *
from playsound import playsound

root = Tk() 
root.geometry('420x500') 
root.title('COUNTDOWN TIMER')
root.configure(bg='black')
root.resizable(False,False)

label1 = Label(root, text='Countdown Timer', fg='black', bg='white', font='arial 20 bold', justify='center')
label1.pack(pady=20)

label2 = Label(root, text=':: set your time!', fg='white', bg='black', font='helvetica 15', justify='left')
label2.place(x=10, y=110)

hrs = StringVar()
hrs_entry = Entry(root, textvariable=hrs, font='arial 60', width=2,state='disabled')
hrs_entry.place(x=20, y=150)
hrs.set('00')

Label(root, text=':', font='arial 60 bold', fg='white', bg='black').place(x=115, y=140)

mins = StringVar()
mins_entry = Entry(root, textvariable=mins, font='arial 60', width=2,state='disabled')
mins_entry.place(x=150, y=150)
mins.set('00')

Label(root, text=':', font='arial 60 bold', fg='white', bg='black').place(x=245, y=140)

sec = StringVar()
sec_entry = Entry(root, textvariable=sec, font='arial 60', width=2,state='disabled')
sec_entry.place(x=280, y=150)
sec.set('00')

label3 = Label(root, text='hours', font='arial 15', fg='white', bg='black').place(x=35, y=250)
label4 = Label(root, text='minutes', font='arial 15', fg='white', bg='black').place(x=155, y=250)
label5 = Label(root, text='seconds', font='arial 15', fg='white', bg='black').place(x=289, y=250)

def increment_time(var, max_val):
    val = int(var.get())
    val += 1
    if val >= max_val:
        val = 0
    var.set(str(val).zfill(2))

def decrement_time(var, max_val):
    val = int(var.get())
    val -= 1
    if val < 0:
        val = max_val - 1
    var.set(str(val).zfill(2))

def update_timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    if times > 0:
        times -= 1
        minutes, seconds = divmod(times, 60)
        hours, minutes = divmod(minutes, 60)
        sec.set(str(seconds).zfill(2))
        mins.set(str(minutes).zfill(2))
        hrs.set(str(hours).zfill(2))
        root.after(1000, update_timer)
    else:
        playsound("C:\\Users\\dutta\\Downloads\\alarm-tone.wav")
        sec.set('00')
        mins.set('00')
        hrs.set('00')
        

Button(root, text='START', bg='white', fg='black', font='arial 21', width=6, height=1, command=update_timer).place(x=140, y=330)

Button(root, text='>', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: increment_time(hrs, 24)).place(x=100, y=250)
Button(root, text='<', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: decrement_time(hrs, 24)).place(x=5, y=250)
Button(root, text='>', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: increment_time(mins, 60)).place(x=240, y=250)
Button(root, text='<', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: decrement_time(mins, 60)).place(x=130, y=250)
Button(root, text='>', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: increment_time(sec, 60)).place(x=370, y=250)
Button(root, text='<', bg='white', fg='black', font='arial 12', width=1, height=1,
       command=lambda: decrement_time(sec, 60)).place(x=265, y=250)

root.mainloop()

