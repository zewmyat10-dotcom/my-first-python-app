import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("My lovely gf")
window.geometry("600x400")
window.resizable(True , True)
image = Image.open("BBBBB.jpg")
image = image.resize((600, 400))
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
label=tk.Label(
    window,text="DO YOU LOVE ME BABY?",
    font=("Arial",20,"bold"),
    bg="#6C26DB",
    fg="Pink",
    padx=20,
    pady=15,
)
label.pack(pady=20)
label1=tk.Label(
    window,text="CAN I BE YOUR MAN?",
    font=("Arial",20,"bold"),
    bg="#6C26DB",
    fg="Pink",
    padx=20,
    pady=15,
)
label1.pack(pady=10)
def CL_BLUE():
    label.config(text="I LOVE YOU TOO BABY " \
    "MWAHHH")
    label1.destroy()
button=tk.Button(
    window,text="YES",command=CL_BLUE,
    padx=30,pady=10,
)
button.pack(pady=20)
def CL_RED():
    label.config(text="PLEASE THINK OF YOUR MIND")
    label1.destroy()
button=tk.Button(
    window,text="NO",command=CL_RED,
    padx=30,pady=10,
)
button.pack()
window.mainloop()