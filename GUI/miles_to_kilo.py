from tkinter import Tk, Label, Entry, Button

window = Tk()
window.title("Miles to Kilometers Converter")

def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.60934  
    km_result_label.config(text=f"{km:.2f}") 

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 16))
equal_label.grid(row=1, column=0)

km_result_label = Label(text="0", font=("Arial", 16))
km_result_label.grid(row=1, column=1)

km_label = Label(text="KM", font=("Arial", 16))
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()
