import tkinter as tk
root = tk.Tk()
#windows = tk.Tk()
root.title("User Login")
#windows.title("Dashboard")
#windows.geometry("1200x800+50+50")
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
#root.geometry("600x400+250+50")
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.resizable(True, False)
root.minsize(400, 200)
root.maxsize(800, 400)
root.attributes('-alpha', 0.8)
#root.attributes('-topmost', True)
root.lower()
#root.iconbitmap("images/ignite.ico")
try:
    photo = tk.PhotoImage(file="images/ignite.png")
    root.iconphoto(False, photo)
except tk.TclError as e:
    print("Error loading icon:", e)

message = tk.Label(root,activeforeground="yellow", text="Enter UserName")
warning = tk.Label(root,activeforeground="red", text="Enter Password")
message.pack()
warning.pack()
root.mainloop()