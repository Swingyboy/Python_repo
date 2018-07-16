from tkinter import *

root = Tk()

label1 = Label(root, text="Title")
label1.grid(row=0, column=0)

label2 = Label(root, text="Author")
label2.grid(row=0, column=2)

label3 = Label(root, text="Year")
label3.grid(row=1, column=0)

label4 = Label(root, text="ISBN")
label4.grid(row=1, column=2)

title_text = StringVar()
entry1 = Entry(root, textvariable=title_text)
entry1.grid(row=0, column=1)

year_text = StringVar()
entry2 = Entry(root, textvariable=year_text)
entry2.grid(row=1, column=1)

author_text = StringVar()
entry3 = Entry(root, textvariable=author_text)
entry3.grid(row=0, column=3)

isbn_text = StringVar()
entry4 = Entry(root, textvariable=isbn_text)
entry4.grid(row=1, column=3)

list1 = Listbox(root, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar1 = Scrollbar(root)
scrollbar1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)

button1 = Button(root, text="View all", width=12)
button1.grid(row=2, column=3)

button2 = Button(root, text="Search entry", width=12)
button2.grid(row=3, column=3)

button3 = Button(root, text="Add entry", width=12)
button3.grid(row=4, column=3)

button4 = Button(root, text="Update", width=12)
button4.grid(row=5, column=3)

button5 = Button(root, text="Delete", width=12)
button5.grid(row=6, column=3)

button6 = Button(root, text="Close", width=12)
button6.grid(row=7, column=3)

root.mainloop()