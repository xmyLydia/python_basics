from tkinter import *
window = Tk()


def kg_convert():
    input = kg_value.get()
    gram = float(input) * 1000
    t1.insert(END, gram)
    pound = float(input) * 2.20462
    t2.insert(END, pound)
    ounce = float(input) * 35.274
    t3.insert(END, ounce)

    #miles = float(kg_value.get())*1.6
    #t1.insert(END, miles)
label = Label(window, text="kg")
label.grid(row=0, column=0)

kg_value = StringVar()
kg_input = Entry(window, textvariable=kg_value)
kg_input.grid(row=0, column=1)


b1 = Button(window, text="Convert", command=kg_convert)
b1.grid(row=0, column=2)

#next line is composed of 3 Text components
labe_gram = Label(window, text="gram")
labe_gram.grid(row=1, column=0)
t1 = Text(window, height=2, width=20)
t1.grid(row=1, column=1)

labe_pound = Label(window, text="pound")
labe_pound.grid(row=1, column=2)
t2 = Text(window, height=2, width=20)
t2.grid(row=1, column=3)

labe_ounce = Label(window, text="ounce")
labe_ounce.grid(row=1, column=4)
t3 = Text(window, height=2, width=20)
t3.grid(row=1, column=5)

window.mainloop()
