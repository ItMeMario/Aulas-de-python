import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Test")

label = tk.Label(root, text="Test", font=('Arial', 18))
label.pack(padx=20,pady=20)
root.mainloop()