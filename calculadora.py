# -*- coding: utf-8 -*-
from Tkinter import*
import tkMessageBox

def Suma():
   n1=float(txt1.get())
   n2=float(txt2.get())
   suma=n1+n2
   tkMessageBox.showinfo("Mensaje","La suma es: %.2f"%suma)
   txt1.delete(0,20)
   txt2.delete(0,20)

def Resta():
   n1=float(txt1.get())
   n2=float(txt2.get())
   resta=n1-n2
   tkMessageBox.showinfo("Mensaje","La resta es: %.2f"%resta)
   txt1.delete(0,20)
   txt2.delete(0,20)

def Multiplicacion():
   n1=float(txt1.get())
   n2=float(txt2.get())
   multiplicacion=n1*n2
   tkMessageBox.showinfo("Mensaje","La multiplicacion es: %.2f"%multiplicacion)
   txt1.delete(0,20)
   txt2.delete(0,20)

def Division():
   n1=float(txt1.get())
   n2=float(txt2.get())
   division=n1/n2
   tkMessageBox.showinfo("Mensaje","La division es: %.2f"%division)
   txt1.delete(0,20)
   txt2.delete(0,20)

pantalla = Tk()
pantalla.title("Programación Avanzada - Calculadora")
pantalla.geometry("400x250+400+200")

#CAJAS DE TEXTO
a = StringVar()
a.set("Escribe el primer numero:")
lbl1 = Label(pantalla, textvariable=a, height = 1)
lbl1.pack()

num1=StringVar()
txt1=Entry(pantalla, bd=4, textvariable=num1)
txt1.pack()

b = StringVar()
b.set("Escribe el segundo numero:")
lbl2 = Label(pantalla, textvariable=b, height = 1)
lbl2.pack()

num2=StringVar()
txt2=Entry(pantalla, bd=4, textvariable=num2)
txt2.pack()

#BOTONES
btn1=Button(pantalla, text="Suma", command=Suma, width=15)
btn1.pack()

btn2=Button(pantalla, text="Resta", command=Resta, width=15)
btn2.pack()

btn3=Button(pantalla, text="Multiplicacion", command=Multiplicacion, width=15)
btn3.pack()

btn4=Button(pantalla, text="Division", command=Division, width=15)
btn4.pack()

nombres = StringVar()
nombres.set("Alexander Figueroa\tRuben Pozo")
lblnom = Label(pantalla, textvariable=nombres, height = 1)
lblnom.pack()

pantalla.mainloop()