import tkinter as tk

root = tk.Tk()

root.geometry('500x400')

root.update()
# root.geometry("500x500")

root.title('Text Translator')

heading = tk.Label(root, text='Text Translator', font=('Poppins', 20))
heading.pack()

root.mainloop()
