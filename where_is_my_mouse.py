import tkinter as tk
import pyautogui
from screeninfo import get_monitors
import ttkbootstrap as ttk

from PIL import Image, ImageTk

import ctypes
from ctypes import wintypes
GWL_STYLE = -16
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000
def get_handle(window):
    return ctypes.windll.user32.GetParent(window.winfo_id())
def disable_minimize_button(window):
    hwnd = get_handle(window)
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
    new_style = current_style & ~WS_MINIMIZEBOX
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, new_style)

root = ttk.Window()
root.title('Where is My Mouse')
root.geometry("320x200")
root.resizable(False, False)

# image_1 = Image.open('D:\\desktop\\marth7.png')
# icon = ImageTk.PhotoImage('D:\\desktop\\Barbara_standard.ico')
# root.iconphoto(True, icon)


label_title = tk.Label(root, text="鼠标指针坐标", font=("Microsoft YaHei", 14))
label_title.pack(side=tk.TOP,pady=10)

frame_main = ttk.Frame(root)
frame_main.pack(side=tk.TOP, fill=tk.X,pady=10)
frame_main.grid_columnconfigure((0,1,2,3),weight=1)

label_x_text = tk.Label(frame_main, text="X:", font=("Arial", 14))
label_x_text.grid(row=1, column=0)

label_x_value = tk.Label(frame_main, text="0", font=("Arial", 14))
label_x_value.grid(row=1, column=1)

label_y_text = tk.Label(frame_main, text="Y:", font=("Arial", 14))
label_y_text.grid(row=1, column=2)

label_y_value = tk.Label(frame_main, text="0", font=("Arial", 14))
label_y_value.grid(row=1, column=3)

monitors = get_monitors()

def update_mouse_position():
    x, y = pyautogui.position()
    label_x_value.config(text=f"{x:.0f}")
    label_y_value.config(text=f"{y:.0f}")
    root.after(10, update_mouse_position)

def toggle_always_on_top():
    if always_on_top_var.get():
        root.attributes('-topmost', 1)
    else:
        root.attributes('-topmost', 0)

always_on_top_var = tk.BooleanVar()
always_on_top_checkbutton = ttk.Checkbutton(root, text="置顶", variable=always_on_top_var,
                                            command=toggle_always_on_top,bootstyle="round-toggle",)
always_on_top_checkbutton.pack(side=tk.TOP,pady=10)

update_mouse_position()

root.after(10, lambda: disable_minimize_button(root))

root.mainloop()
