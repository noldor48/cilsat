from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("Project")
root.iconbitmap(default="useri.ico")
root.geometry("300x250")

label0 = ttk.Label()
label0.pack(anchor=NW, padx=6, pady=6)
label0["text"] = "1. Pievienot cilveku \n2. Paradit visus cilvekus \n3. Meklet cilveku \n4. Iziet"

def right():
    label1["text"] = "N"

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="Click", command=right)
btn.pack(anchor=NW, padx=6, pady=6)
 
label1 = ttk.Label()
label1.pack(anchor=NW, padx=6, pady=6)

root.mainloop()