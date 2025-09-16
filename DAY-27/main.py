from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("miles to km converter")
window.config(padx=20, pady=20)



def calculate():
    pass
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    result.config(text=f"{km}" )

mile_txt = Label(text="miles", font=("Arial", 24, "bold"))
mile_txt.grid(column=2, row=0)

equal_txt = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_txt.grid(column=0, row=1)

result = Label(text=0, font=("Arial", 24, "bold"))
result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)




window.mainloop()