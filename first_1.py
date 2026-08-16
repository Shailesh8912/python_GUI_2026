import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("800x400+50+50")
root.resizable(False, False)
root.title("Tkinter Image Button")

def on_button_click():
    showinfo(
        title="Information",
        message="You clicked the image button!"
    )
# donwloaded_image = tk.PhotoImage(file="images/play.png", width=50, height=50)  # Adjust the width and height as needed
# image_button = tk.Button(root, image=donwloaded_image, command=on_button_click)
# image_button.pack(pady=20)

root.mainloop()