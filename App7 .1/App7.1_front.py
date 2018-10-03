from tkinter import *
import App7_back


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in App7_back.view():
        list1.insert(END, row)
    return 0


def search_command():
    list1.delete(0, END)
    for row in App7_back.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
    return 0


def add_command():
    App7_back.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    return 0


def delete_command():
    App7_back.delete(selected_tuple[0])
    return 0


def update_command():
    App7_back.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    return 0


root = Tk()

root.wm_title("BookStore")

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

list1.bind('<<ListboxSelect>>', get_selected_row)

button1 = Button(root, text="View all", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(root, text="Search entry", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(root, text="Add entry", width=12, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(root, text="Update", width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(root, text="Delete", width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(root, text="Close", width=12, command=root.destroy)
button6.grid(row=7, column=3)

root.mainloop()