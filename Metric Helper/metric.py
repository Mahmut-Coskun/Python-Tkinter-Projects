#Metric Helper
import tkinter
from tkinter import ttk, END

root = tkinter.Tk()
root.title("Metric Helper")
root.iconbitmap("ruler.ico")
root.resizable(0,0)

#Define fonts and Colors
field_font = ("Cambria", 10)
bg_color = "#c75c7c"
button_color = "#f5cf87"
root.config(bg = bg_color)

#Define Functions
def clear_default_text(event):
    """Clear the default text when user clicks on the input field."""
    if input_field.get() == "Enter your quantity":
        input_field.delete(0, END)
        input_field.config(fg='black')  # Change text color to black

def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
        "femto":10**-15,
        "pico":10**-12,
        "nano":10**-9,
        "micro":10**-6,
        "milli":10**-3,
        "centi":10**-2,
        "deci":10**-1,
        "base value":10**0,
        "deca":10**1,
        "hecta":10**2,
        "kilo":10**3,
        "mega":10**6,
        "giga":10**9,
        "tera":10**12,
        "peta":10**15
    }

    #Clear the output field
    output_field.delete(0,END)

    #Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    #Convert to the base unit first
    base_value = start_value * metric_values[start_prefix]

    #Convert to new metric value
    end_value = base_value / metric_values[end_prefix]

    #Update output field with answer
    output_field.insert(0,str(end_value))

#Define Layout
#Make the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3, fg='grey')
output_field = tkinter.Entry(root, width=20, font=field_font,borderwidth=3)
equal_label = tkinter.Label(root, text = "=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row = 0, column=1,padx=10,pady=10)
output_field.grid(row = 0, column=2,padx=10,pady=10)

input_field.insert(0, "Enter your quantity")
input_field.bind("<FocusIn>", clear_default_text)

#Make dropdown for metric values
metric_list = ["femto","pico","nano","micro","milli","centi","deci","base value","deca","hecta","kilo","mega","giga","tera","peta"]
input_combobox = ttk.Combobox(root,value = metric_list,font=field_font, justify="center")
output_combobox = ttk.Combobox(root,value = metric_list, font=field_font, justify="center")
to_label = tkinter.Label(root, text ="to", font=field_font, bg = bg_color)

input_combobox.grid(row=1, column=0,padx=10,pady=10)
to_label.grid(row=1,column=1,padx=10,pady=10)
output_combobox.grid(row=1, column=2,padx=10,pady=10)

input_combobox.set("base value")
output_combobox.set("base value")

#Make a conversion button
convert_button = tkinter.Button(root, text = "Convert", font=field_font, bg = button_color,command=convert)
convert_button.grid(row=2,column=0,columnspan=3,padx=10,pady=10,ipadx=50)



# Run the root window's main loop
root.mainloop()