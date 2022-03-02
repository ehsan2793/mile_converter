from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500,height=500)
window.config(padx=20 , pady=20)

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer = Label(text="0")
kilometer.grid(column=1,row=1)

kilometer_unit = Label(text="Km")
kilometer_unit.grid(column=2,row=1)

calculate = Button(text="Calculate")
calculate.grid(column=1,row=2)

window.mainloop()
