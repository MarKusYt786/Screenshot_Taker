import pyautogui 
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title("CAMERA")
Canvas1 = tk.Canvas(root,width=300,height=300)
Canvas1.pack()

def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path +".png")
    
myButton = tk.Button(text="Take Screenshot",command=takeScreenshot,font=10)
Canvas1.create_window(150,150,window=myButton)

root.mainloop()