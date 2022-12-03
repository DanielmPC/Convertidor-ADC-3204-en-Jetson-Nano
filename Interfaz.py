# Antes de correr el programa ejecutar:
#   sudo modprobe spidev

#!/usr/bin/python3.7

from tkinter import Tk, Frame, Button, Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #posiciona la grafica en tkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import *
from Lec_sensor import chan
import matplotlib.animation as animation
import math


xdatos, ydatos = [], []
#f = r"/home/nvidia/Documentos/Python/25-11-22/animation.gif"
wd = 10

def animate(i, xdatos, ydatos):
    datos = chan.voltage
    xdatos.append(i)
    ydatos.append(datos)
    ax.clear()
    ax.plot(xdatos, ydatos)
    #Redondeamos el valor 
    def truncate(datos, cifras=2):
        posiciones = pow(10.0, cifras)
        return math.trunc(posiciones * datos)/posiciones

    label.config(text=truncate(datos))

def graficar_datos():
    global ani
    ani = animation.FuncAnimation(fig, animate, fargs=(xdatos, ydatos))
    
    canvas.draw()
    
def pausa():
    ani.event_source.stop()

def reanudar():
    ani.event_source.start()

"""
def guardar():
    writegif = animation.PillowWriter(fps=30)
    ani.save(f,writer=writegif)
"""
def salir():
    ventana.destroy()
    ventana.quit()
    print("Cerrando ventana...")


# creamos la grafica
fig = plt.figure(dpi=90, figsize=(7,5), facecolor='#181F32')#00faafb7
ax = fig.add_subplot(1,1,1)
#plt.title("Gráfica en Tkinter con matplotlib", color='#EDE3E0', size=16, family="arial")

#plt.xlim(-4,14)
plt.ylim(-2,4)
ax.set_facecolor('#EDE3E0')

#configuramos los ejes de la grafica
ax.axhline(linewidth=2, color='gray')
ax.axvline(linewidth=1.5, color='gray')

#configuramos los separadores
ax.set_xlabel("Eje horizontal", color='#EDE3E0')
ax.set_ylabel("Eje vertical", color='#EDE3E0')
#configuramos los números que salen en los separadores
ax.tick_params(direction='out', length=6, width=2, colors='#EDE3E0', grid_color='r', grid_alpha=0.5)


#Creamos la ventana con Tkinter
ventana = Tk()
ventana.geometry("642x500")
ventana.title("Graficadora ADC converter")
ventana.minsize(width=642, height=500)

# creamos el frame donde almacenamos la gráfica
frame = Frame(ventana, bg='#7D7A73', bd=3)
frame.grid(column=0, row=0)

#creamos el area de dibujo 
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(column=0, row=0, columnspan=5, padx=6, pady=5)

#creamos el boton de graficar 
Button(frame, text="Encender", width=wd, bg='#941F48', fg='#EDE3E0', command=graficar_datos).grid(column=0, row=1, pady=3)

#label = Label(frame, width=9)
#label.grid(column=3, row=1, pady=3)

#creamos el boton de pausa 
Button(frame, text="Pausa", width=wd, bg='#E7BA29', fg='#EDE3E0', command=pausa).grid(column=1, row=1, pady=5)

#label = Label(frame, width=15)
#label.grid(column=2, row=1, pady=5)

#creamos el boton de reanudar
Button(frame, text="Reanudar", width=wd, bg='green', fg='#EDE3E0', command=reanudar).grid(column=2, row=1, pady=5)

#creamos el boton de salir 
Button(frame, text="Salir", width=wd, bg='red', fg='#EDE3E0', command=salir).grid(column=3, row=1, pady=5)

label = Label(frame, width=8)
label.grid(column=4, row=1, pady=5)


style = ttk.Style()
style.configure("Horizontal.TScale", background='green')

'''scale = ttk.Scale(frame, to=6, from_=0, orient='horizontal', length=300)
scale.grid(column=2, row=1)'''

ventana.mainloop()