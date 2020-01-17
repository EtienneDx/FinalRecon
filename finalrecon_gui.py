import os
import tkinter as tk


root = tk.Tk()
root.title("Final Recon")
root.geometry("400x200")

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text="Url: ").pack(side=tk.LEFT)
url = tk.Entry(frame1, width=40)
url.pack(side=tk.RIGHT)

tk.Button(text="Headers", command=lambda: os.system("python finalrecon.py {} --headers > output.txt".format(url.get()))).pack()
tk.Button(text="SSL Infos", command=lambda: os.system("python finalrecon.py {} --sslinfo".format(url.get()))).pack()
tk.Button(text="Who Is", command=lambda: os.system("python finalrecon.py {} --whois".format(url.get()))).pack()
tk.Button(text="Crawl", command=lambda: os.system("python finalrecon.py {} --crawl".format(url.get()))).pack()
tk.Button(text="Alls", command=lambda: os.system("python finalrecon.py {} --full".format(url.get()))).pack()

root.mainloop()
