from tkinter import *

root = Tk()

def convert_weight():
    grams = 1000 * float(weightValue.get())
    pounds = 2.20462 * float(weightValue.get())
    ounces = 35.274 * float(weightValue.get())
    gramsWeight.delete("1.0", END)
    gramsWeight.insert(END, grams)
    poundsWeight.delete("1.0", END)
    poundsWeight.insert(END, pounds)
    ouncesWeight.delete("1.0", END)
    ouncesWeight.insert(END, ounces)

myLabel = Label(root, text = "Kg")
myLabel.grid( row = 0, column = 0)

weightValue = StringVar()
weight = Entry(root, textvariable = weightValue)
weight.grid(row = 0, column = 1)

myButton = Button(root, text = "Convert", command = convert_weight)
myButton.grid(row = 0, column = 2)

gramsWeight = Text(root, height = 1, width = 20)
gramsWeight.grid(row = 1, column = 0)

poundsWeight = Text(root, height = 1, width = 20)
poundsWeight.grid(row = 1, column = 1)

ouncesWeight = Text(root, height = 1, width = 20)
ouncesWeight.grid(row = 1, column = 2)

root.mainloop()