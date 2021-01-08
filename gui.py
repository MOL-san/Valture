from tkinter import *


tk = Tk()
tk.geometry("500x500")
canvas = Canvas(bg="#008000", width=500, height=500)
canvas.pack()
tk.configure(background="#008000")
tk.title("ハゲタカのえじき")

back = PhotoImage(file="images/card_back.png")
canvas.create_image(250, 150, image=back)
canvas.create_text(250, 50, text="山札", font=(
    "HiraMaruProN - W4", 30), fill="white")

tk.mainloop()
