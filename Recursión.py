import random 
from tkinter import*
class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x200")
        self.config(bg="mediumturquoise")
        self.lb1=Label(self,text="Recursión Factorial - Fibonacci", font="Arial 15 underline", bg="mediumturquoise")
        self.lb1.place(x=75,y=10)
        self.c=Entry(self, width=10)
        self.c.place(x=200,y=50)
        self.lb=Label(self,text="Ingrese un número", font="Arial 9", bg="mediumturquoise")
        self.lb.place(x=80,y=50)
        self.tfac=StringVar()
        self.lb4=Label(self,text="Valor Factorial", font="Arial 9", bg="mediumturquoise")
        self.lb4.place(x=80,y=80)
        self.c3=Entry(self, width=15, state=DISABLED,textvariable=self.tfac)
        self.c3.place(x=200,y=80)
        self.tfib=StringVar()
        self.lb3=Label(self,text="Termino Fibonacci", font="Arial 9", bg="mediumturquoise")
        self.lb3.place(x=80,y=110)
        self.c2=Entry(self, width=15, state=DISABLED,textvariable=self.tfib)
        self.c2.place(x=200,y=110)
        self.b1=Button(self,text="Termino Fibonacci", command=self.do)
        self.b1.place(x=120,y=140)
        self.mainloop()
    def do(self):
        n1=int(self.c.get())
        self.tfac.set(str(self.fact(n1)))
        self.tfib.set(str(self.fibo(n1)))
    def fact(self,n):
        if n==0:
            return 1
        else:
            return n* self.fact(n-1)
    def fibo(self,n):
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return self.fibo(n-1)+self.fibo(n-2)
app=forma()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Comenzar el uso de recursiones
#Lenguaje: Python
#Net Framewor: 4.5
#Recursos: visual code
#Descripción: Desarrollar un programa que calule el factorial del numero ingresado y el elemento en la sucesion de fibonacci
#Ultima modificación 24/03/2021
#HEY SOY UNA PRUEBA
