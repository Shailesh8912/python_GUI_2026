import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("800x400+50+50")
root.resizable(False, False)
root.title("Tkinter Checkbutton Example")

def show_message():
    
    showinfo(
       title="Information",
        message=f"You agreed" if agreement_var.get() else "You disagreed"
    )

agreement_var = tk.BooleanVar()

checkbox=ttk.Checkbutton(
    root,
    text="I agree to the terms and conditions",
    variable=agreement_var,
    command=show_message
)
checkbox.pack(pady=20)

txt_name=tk.StringVar()
txt_subject=tk.StringVar()
txt_password=tk.StringVar()

name_label=tk.Label(root,text="Enter your name")
name_label.pack(pady=2)
name=tk.Entry(root, textvariable=txt_name)
name.pack(pady=5)
name.focus()


Subject_label=tk.Label(root,text="Enter your subject")
Subject_label.pack(pady=2)
Subject=tk.Entry(root, textvariable=txt_subject)
Subject.pack(pady=5)

password_label=tk.Label(root,text="Enter your password")
password_label.pack(pady=2)
password=tk.Entry(root, textvariable=txt_password, show="*")
password.pack(pady=5)
submit_button=tk.Button(root,
                        text="Submit",
                        command=lambda: 
                        showinfo(
                            title="Information",
                            message=f"Name: {txt_name.get()} \n Subject: {txt_subject.get()} \n Password: {txt_password.get()}"))

submit_button.pack(pady=10)

output_label1=tk.Label(root,text="Output")
output_label1.pack(pady=2)
output_label2=tk.Label(root,text="Output")
output_label2.pack(pady=2)
output_label3=tk.Label(root,text="Output")
output_label3.pack(pady=2)


txt_name.trace_add("write", lambda *args: output_label1.config(text=f"Name changed to: {txt_name.get()}"))
txt_subject.trace_add("write", lambda *args: output_label2.config(text=f"Subject changed to: {txt_subject.get()}"))
txt_password.trace_add("write", lambda *args: output_label3.config(text=f"Password changed to: {txt_password.get()}"))



root.mainloop()