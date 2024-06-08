import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("780x480+600+150")
app.title("Temperature Converter")
app.resizable(False, False)

f = ctk.CTkFrame(
    app,
    width=750,
    height=450,
    corner_radius=10
)
f.place(x=15, y=15)

lbl = ctk.CTkLabel(
    f,
    text="Temperature Converter",
    font=("Poppins", 20, "bold"),
    text_color="white",
    fg_color="#2b2b2b"
)
lbl.place(x=30, y=30)

cel_entry = ctk.CTkEntry(
    f,
    width=400,
    height=50,
    font=("Poppins", 15, "bold"),
)
cel_entry.place(x=40, y=110)

cel_lbl = ctk.CTkLabel(
    f,
    text="°C",
    font=("Poppins", 45, "bold"),
    text_color="white",
    fg_color="#2b2b2b"
)
cel_lbl.place(x=450, y=95)

far_entry = ctk.CTkEntry(
    f,
    width=400,
    height=50,
    font=("Poppins", 15, "bold"),
)
far_entry.place(x=40, y=200)

far_lbl = ctk.CTkLabel(
    f,
    text="°F",
    font=("Poppins", 45, "bold"),
    text_color="white",
    fg_color="#2b2b2b"
)
far_lbl.place(x=450, y=188)

kel_entry = ctk.CTkEntry(
    f,
    width=400,
    height=50,
    font=("Poppins", 15, "bold"),
)
kel_entry.place(x=40, y=290)

kel_lbl = ctk.CTkLabel(
    f,
    text="K",
    font=("Poppins", 45, "bold"),
    text_color="white",
    fg_color="#2b2b2b"
)
kel_lbl.place(x=460, y=275)

conv_btn = ctk.CTkButton(
    f,
    width=70,
    height=40,
    text="Convert",
    hover=False,
    font=("Poppins", 20, "bold"),
    fg_color="#74E291",
    text_color="black",
    command=lambda: convert()
)
conv_btn.place(x=100, y=370)

clear_btn = ctk.CTkButton(
    f,
    width=100,
    height=40,
    text="Clear",
    hover=False,
    font=("Poppins", 20, "bold"),
    fg_color="#EE4E4E",
    text_color="black",
    command=lambda: clear()
)
clear_btn.place(x=250, y=370)

def convert():
    try:
        if cel_entry.get():
            c = float(cel_entry.get())
            f = (c * 9/5) + 32
            k = c + 273.15
            far_entry.delete(0, "end")
            far_entry.insert(0, f)
            kel_entry.delete(0, "end")
            kel_entry.insert(0, k)
        elif far_entry.get():
            f = float(far_entry.get())
            c = (f - 32) * 5/9
            k = c + 273.15
            cel_entry.delete(0, "end")
            cel_entry.insert(0, c)
            kel_entry.delete(0, "end")
            kel_entry.insert(0, k)
        elif kel_entry.get():
            k = float(kel_entry.get())
            c = k - 273.15
            f = (c * 9/5) + 32
            cel_entry.delete(0, "end")
            cel_entry.insert(0, c)
            far_entry.delete(0, "end")
            far_entry.insert(0, f)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

def clear():
    far_entry.delete(0, "end")
    kel_entry.delete(0, "end")
    cel_entry.delete(0, "end")

app.after(100, cel_entry.focus_set)
app.mainloop()
