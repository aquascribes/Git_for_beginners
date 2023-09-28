from tkinter import Tk, Label

window=Tk()
window.title("Window")
window.geometry("600x300")
window.configure(bg="blue")

label=Label(window,text="welcome",font=("Arial Black",78,"bold"),bg="blue")
label.pack(pady=100)
window.mainloop()
