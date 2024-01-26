import tkinter


window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=50)


def convert():
    miles = float(mile_to_convert.get())
    km = round(miles * 1.609, 2)
    km_converted_label.config(text=km)


miles_label = tkinter.Label(text="mi")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_converted_label = tkinter.Label(text="0")
km_converted_label.grid(column=1, row=1)

mile_to_convert = tkinter.Entry(width=10, justify="center")
mile_to_convert.grid(column=1, row=0)

my_button = tkinter.Button(text="Calculate", command=convert)
my_button.grid(column=1, row=2)

window.mainloop()