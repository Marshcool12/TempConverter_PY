import tkinter as tk
window=tk.Tk()
window.title("Temprature Converter")
window.configure(bg="light grey")
window.resizable(width=False, height=False)
window.geometry("600x800")
#------------------------------------------------------------------------------------------------------------
#ALL DEFINITIONS
def concel():
    try:
        #checks if the box is empty
        if str(inpval_ent.get()) == "":
            result_lbl["text"] = str("Invalid Input")
        else:
            #otherwise it will turn it into float and convert it to celsius
            result_lbl["text"] = str(round((float(inpval_ent.get()) - 32) * (5/9))) + "°C"
    except ValueError:
        #if the value isnt float then it will print invalid input
        result_lbl["text"] = str("Invalid Input")

def confah():
    try:
        #checks if the box is empty
        if str(inpval_ent.get()) == "":
            result_lbl["text"] = str("Invalid Input")
        else:
            #otherwise it will turn it into float and convert it to fahrenheit
            result_lbl["text"] = str(round((float(inpval_ent.get()) * (9/5)) + 32)) + "°F"
    except ValueError:
        #if the value isnt float then it will print invalid input
        result_lbl["text"] = str("Invalid Input")

#------------------------------------------------------------------------------------------------------------
#ALL WIDGETS

#the label directing u to the input area
inplabel_lbl = tk.Label(text="Enter Value To Convert Below", font=("Times New Roman", 16))
inplabel_lbl.pack(expand=True, padx=5, pady=5)

#entry box for ur value that u want to conv
inpval_ent = tk.Entry(font=("Bold", 32))
inpval_ent.pack(expand=True, padx=10, pady=10)

#btn to convert to celsius
cel_btn = tk.Button(text="convert to celsius", command=concel, background="light blue", font=("Bold",16))
cel_btn.pack(expand=True, padx=5, pady=5)

#btn to convert to fahrenheit
fah_btn = tk.Button(text="convert to faherenheit", command=confah, background="light pink", font=("Bold",16))
fah_btn.pack(expand=True, padx=5, pady=5)

#the result label which will change to the value u want
result_lbl = tk.Label(text="result", font=("Bold",32))
result_lbl.pack(expand=True)

#------------------------------------------------------------------------------------------------------------
#LOOPS THE WINDOW
window.mainloop()