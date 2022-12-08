from tkinter import *


root=Tk()
root.resizable(0,0)
root.config(bg="black")
root.title("Calculadora")

# MARCO o FRAME
marco=Frame(root,bg="violet",width="650",height="350")
marco.pack(fill="none",expand="True")

root.mainloop()