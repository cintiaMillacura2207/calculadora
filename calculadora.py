from tkinter import *


root=Tk()
root.resizable(0,0)
root.config(bg="black")
root.title("Calculadora")

# MARCO o FRAME
marco=Frame(root,bg="violet",width="650",height="350")
marco.pack(fill="none",expand="True")

pantalla=Entry(marco)
pantalla.grid(row=0,columnspan=5,sticky=W+E,pady=5,padx=3)
pantalla.config(bg="lightblue",fg="black",width=30,font=("Arial",18,'bold'),borderwidth=2,relief="solid",
               justify=RIGHT)

root.mainloop()