import tkinter as tk
import os
from tkinter import ttk
from tkinter.constants import CENTER
from tkinter import filedialog as fido
import pyscreenshot as ImageGrab

BRAT = "#86C800"

def main():
    root = tk.Tk()
    root.geometry("680x640")
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
    tk.Button(controls, text="Save", command=lambda: save(), bg=BRAT).grid(column=3, row=0, padx=20)
    tk.Button(controls, text="Quit", command=root.destroy, bg=BRAT).grid(column=4, row=0, padx=20)

    def save(*event):
        filename = fido.asksaveasfilename(title = "Create Image", filetypes=(("PNG Image", ".png"),))
        if filename:
            if not os.path.exists(filename):
                path, file = os.path.split(filename)
                name, ext = os.path.splitext(file)
                if ext.lower() in ['.gif', '.png']:
                    x1 = root.winfo_rootx() + brat_frame.winfo_x()
                    y1 = root.winfo_rooty() + brat_frame.winfo_y()
                    x2 = x1 + brat_frame.winfo_width()
                    y2 = y1 + brat_frame.winfo_height()
                    image = ImageGrab.grab().crop((x1, y1, x2, y2))
                    image.save(filename)
                    print(f"Saved image {file}")
                else:
                    print("Unknown file type")

    root.bind("<Control-s>", save)
    root.mainloop()


if (__name__ == "__main__"):
    main()
