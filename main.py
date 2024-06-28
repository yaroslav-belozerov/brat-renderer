import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER

BRAT = "#86C800"

def main():
    root = tk.Tk()
    root.geometry("560x640")
    frame = ttk.Frame(root, padding=30)
    frame.grid()
    
    controls = ttk.Frame(frame)
    controls.grid(pady=20)
    brat_frame = tk.Frame(frame, width=500, height=500, bg=BRAT) 
    brat_frame.grid()
    brat_txt = tk.Label(brat_frame, text="brat", wraplength=500, font=("Arial", 100), bg=BRAT)
    brat_txt.place(relx=.5, rely=.5, anchor=CENTER)

    title = ttk.Label(controls, text="brat 1.0")
    title.grid(column=0, row=0, padx=20)
    inp = tk.Text(controls, height=1, width=20)
    inp.grid(column=1, row=0, padx=20)

    def get_text():
        txt = inp.get("1.0",'end-1c')
        brat_txt.config(text = txt)

    tk.Button(controls, text="Apply", command=lambda: get_text(), bg=BRAT).grid(column=2, row=0, padx=20)
    tk.Button(controls, text="Quit", command=root.destroy, bg=BRAT).grid(column=3, row=0, padx=20)

    root.mainloop()



if (__name__ == "__main__"):
    main()
