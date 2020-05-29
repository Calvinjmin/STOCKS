# Reference for tkinter - https://realpython.com/python-gui-tkinter/
import tkinter as tk

window = tk.Tk()
window.title("STOCKS")

window.geometry("500x500")
window.resizable(0,0)

frame = tk.Frame(master=window)
frame.pack_propagate(0)
frame.pack(fill=tk.BOTH, expand=1)

text = tk.Label(text="Test")
text.pack()

window.mainloop()
