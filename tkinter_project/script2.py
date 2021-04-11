from tkinter import *
window = Tk()


def kg_convert():
    print(kg_value.get())

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


window.mainloop()
