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

#BUTTONS NUMEROS

boton_1=Button(marco,text="1",command=lambda:envia_boton(1))
boton_1.grid(row=6,column=0,sticky=W+E,pady=1,padx=1)
boton_1.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_2=Button(marco,text="2",command=lambda:envia_boton(2))
boton_2.grid(row=6,column=1,sticky=W+E,pady=1,padx=1)
boton_2.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_3=Button(marco,text="3",command=lambda:envia_boton(3))
boton_3.grid(row=6,column=2,sticky=W+E,pady=1,padx=1)
boton_3.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_4=Button(marco,text="4",command=lambda:envia_boton(4))
boton_4.grid(row=5,column=0,sticky=W+E,pady=1,padx=1)
boton_4.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_5=Button(marco,text="5",command=lambda:envia_boton(5))
boton_5.grid(row=5,column=1,sticky=W+E,pady=1,padx=1)
boton_5.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_6=Button(marco,text="6",command=lambda:envia_boton(6))
boton_6.grid(row=5,column=2,sticky=W+E,pady=1,padx=1)
boton_6.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_7=Button(marco,text="7",command=lambda:envia_boton(7))
boton_7.grid(row=4,column=0,sticky=W+E,pady=1,padx=1)
boton_7.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_8=Button(marco,text="8",command=lambda:envia_boton(8))
boton_8.grid(row=4,column=1,sticky=W+E,pady=1,padx=1)
boton_8.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_9=Button(marco,text="9",command=lambda:envia_boton(9))
boton_9.grid(row=4,column=2,sticky=W+E,pady=1,padx=1)
boton_9.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

boton_0=Button(marco,text="0",command=lambda:envia_boton(0))
boton_0.grid(row=7,column=1,columnspan=2,sticky=W+E,pady=1,padx=1)
boton_0.config(width=5,height=2, bg="yellow",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#BUTTONS OPERACIONES

#Boton borrar
boton_AC=Button(marco,text="AC",command=borrar)
boton_AC.grid(row=4,column=4,sticky=W+E,pady=1,padx=1)
boton_AC.config(width=5,height=2, bg="red",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton M+
boton_M=Button(marco,text="M+",command=cargar_datos)
boton_M.grid(row=5,column=4,sticky=W+E,pady=1,padx=1)
boton_M.config(width=5,height=2, bg="red",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton M-
boton_B=Button(marco,text="M-",command=borrar_Datos)
boton_B.grid(row=5,column=3,sticky=W+E,pady=1,padx=1)
boton_B.config(width=5,height=2, bg="black",fg="white",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton suma
boton_Suma=Button(marco,text="+",command=suma)
boton_Suma.grid(row=6,column=3,sticky=W+E,pady=1,padx=1)
boton_Suma.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton resta
boton_Resta=Button(marco,text="-",command=resta)
boton_Resta.grid(row=6,column=4,sticky=W+E,pady=1,padx=1)
boton_Resta.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton multiplicacion
boton_Mult=Button(marco,text="*",command=multiplicacion)
boton_Mult.grid(row=7,column=3,sticky=W+E,pady=1,padx=1)
boton_Mult.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")

#Boton division
boton_Div=Button(marco,text="/",command=division)
boton_Div.grid(row=7,column=4,sticky=W+E,pady=1,padx=1)
boton_Div.config(width=5,height=2, bg="lightblue",fg="black",font=("Arial",12),cursor="hand2",borderwidth=3, relief="ridge")




root.mainloop()