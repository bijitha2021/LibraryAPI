from tkinter import *
from AddBook import *

mainView = Tk()
mainView.title("Library Management System")
mainView.geometry("800x600")

Canvas1 = Canvas(mainView)
Canvas1.config(bg="light blue")
Canvas1.pack(expand=True, fill=BOTH)
Canvas1.create_image(10, 10, anchor=NW)

headingFrame1 = Frame(mainView, bg="#FFBB02", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Library Management", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(mainView, text="Add Book ", bg='black', fg='white', font=('Courier', 12),command=addBook)#, command=addBook
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(mainView, text="Delete Book", bg='black', fg='white', font=('Courier', 12) )
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(mainView, text="View & Issue Books", bg='black', fg='white', font=('Courier', 12))
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(mainView, text="Return Book", bg='black', fg='white', font=('Courier', 12))
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(mainView, text="Exit", bg='black', fg='white', font=('Courier', 12), command=mainView.destroy)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

mainView.mainloop()
