import tkinter as tk

root = tk.Tk()
root.title("Frame and LabelFrame")
def loginwindow():
    loginroot = tk.Toplevel(root)
    loginroot.title("Login Window")
    tk.Label(loginroot, text="Username:").grid(row=0, column=0, sticky="w")
    tk.Entry(loginroot).grid(row=0, column=1) 
    tk.Label(loginroot, text="Password:").grid(row=1, column=0, sticky="w")
    tk.Entry(loginroot, show="*").grid(row=1, column=1)
    tk.Button(loginroot, text="Login").grid(row=2, column=0, columnspan=2)

personal_frame = tk.LabelFrame(root, text="Personal Details", padx=10, pady=10)
personal_frame.pack(padx=10, pady=10, fill="x")

tk.Label(personal_frame, text="Name:").grid(row=0, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=0, column=1)
tk.Label(personal_frame, text="Age:").grid(row=1, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=1, column=1)
tk.Label(personal_frame, text="Gender:").grid(row=2, column=0, sticky="w")
tk.Entry(personal_frame).grid(row=2, column=1)

academic_frame = tk.LabelFrame(root, text="Academic Details", padx=10, pady=10)
academic_frame.pack(padx=10, pady=10, fill="x")

tk.Label(academic_frame, text="Course:").grid(row=0, column=0, sticky="w")
tk.Entry(academic_frame).grid(row=0, column=1)
tk.Label(academic_frame, text="Year:").grid(row=1, column=0, sticky="w")
tk.Entry(academic_frame).grid(row=1, column=1)
tk.Label(academic_frame, text="University:").grid(row=2, column=0, sticky="w")
tk.Entry(academic_frame).grid(row=2, column=1)

submit_frame = tk.Frame(root, padx=10, pady=10)
submit_frame.pack(padx=10, pady=10, fill="x")
submit_button = tk.Button(submit_frame, text="Submit", command=loginwindow)
submit_button.pack()




root.mainloop()