from tkinter import Tk, Label

window=Tk()
window.title("digital clock")
window.geometry("600x300")
window.configure(bg="red")

label=Label(window,text="welcome",font=("Arial Black",78,"bold"),bg="red")
label.pack(pady=100)
window.mainloop()
