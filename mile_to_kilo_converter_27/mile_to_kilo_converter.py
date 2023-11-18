from tkinter import *

def miles_to_km():
    miles=float(mile_input.get())
    km=miles*1.689
    Kilometer_result_label.config(text=f"{km}")
    
    
    
window=Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20,pady=20)

mile_input=Entry(width=7)
mile_input.grid(column=1,row=0)

mile_lable=Label(text="Miles")
mile_lable.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

Kilometer_result_label=Label(text="0")
Kilometer_result_label.grid(column=1,row=1)

kilometer_label=Label(text="KM")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(text="calculater",command=miles_to_km)
calculate_button.grid(column=1,row=2)


window.mainloop()