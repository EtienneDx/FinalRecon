import os
import sys
import tkinter as tk
from tkinter import ttk

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3.x!")

root = tk.Tk()
root.title("Final Recon")
root.geometry("400x200")

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text="Url: ").pack(side=tk.LEFT)
url = tk.Entry(frame1, width=40)
url.pack(side=tk.RIGHT)

frame2 = tk.Frame(root)
frame2.pack()

tk.Label(frame2, text="Target: ").pack(side=tk.LEFT)
target = ttk.Combobox(frame2, values=["Console", "File"])
target.current(0)
target.pack(side=tk.RIGHT)


def get_target():
    return "" if target.get() == "Console" else " > output.txt"


tk.Button(text="Headers", command=lambda:
               os.system("{} finalrecon.py {} --headers{}".format(sys.executable, url.get(), get_target()))).pack()
tk.Button(text="SSL Infos", command=lambda:
               os.system("{} finalrecon.py {} --sslinfo{}".format(sys.executable, url.get(), get_target()))).pack()
tk.Button(text="Who Is", command=lambda:
               os.system("{} finalrecon.py {} --whois{}".format(sys.executable, url.get(), get_target()))).pack()
tk.Button(text="Crawl", command=lambda:
               os.system("{} finalrecon.py {} --crawl{}".format(sys.executable, url.get(), get_target()))).pack()
tk.Button(text="Alls", command=lambda:
               os.system("{} finalrecon.py {} --full{}".format(sys.executable, url.get(), get_target()))).pack()

root.mainloop()
