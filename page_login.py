import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("450x160+50+50")
root.resizable(False, False)
root.title("Login Form")
root.configure(bg="lightblue")

root.rowconfigure(0,weight=10)
root.rowconfigure(2,weight=10)
root.rowconfigure(4,weight=10)
root.columnconfigure(0,weight=10)
root.columnconfigure(1,weight=10)

ulabel=tk.Label(root,text="Enter Username",bg="lightblue")
ulabel.grid(row=0,column=0,padx=1,pady=1)
txtUsername=tk.Entry(root)
txtUsername.grid(row=0,column=1,padx=1,pady=1)

plabel=tk.Label(root,text="Enter Password",bg="lightblue")
plabel.grid(row=2,column=0,padx=1,pady=1)
txtPassword=tk.Entry(root,show="*")
txtPassword.grid(row=2,column=1,padx=1,pady=1)

submit_btn=tk.Button(root,text="Submit")
#submit_btn.grid(row=2,column=0,columnspan=2,sticky=tk.EW,padx=5,pady=5)
submit_btn.grid(row=4,column=1,padx=1,pady=1)


root.mainloop()