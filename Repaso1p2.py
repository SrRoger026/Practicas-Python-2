

from tkinter import *
from tkinter import messagebox
from validarrepaso import Validar


class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.lista = []
        self.valid = Validar()
        

    def inicio(self):
        Label(self.ventana, text="Programa de python con TKInter").place(x=100, y=20)# x = columna y= fila
        Label(self.ventana, text="Escribe un dato").place(x=50, y=50)
        self.dato = Entry(self.ventana)
        self.dato.place(x=150, y=50, width=150)
        Button(self.ventana, text="Validar", command=self.ValidarDatos).place(x=150, y=90, width=150)
        self.mostrar = Label(self.ventana, text="ejemplo")
        self.mostrar.place(x=20, y=150)
        self.ventana.mainloop()

    def ValidarDatos(self):
        val = self.dato.get()
        if val != "":
            self.Revisar(val)
            self.lista.append(val)
            self.dato.delete(0,END)
            # print(self.lista)
            self.mostrar.config(text=f'{self.lista}')
            # respuesta = self.valid.ValidarAscii(val)
            # respuesta = self.valid.ValidarConError(val)
            respuesta = self.valid.ValidarConString(val)
            messagebox.showinfo("Validar Datos", f'El dato es {respuesta}')
        else:
            messagebox.showerror("Error","Caja de texto esta vacia")

    def Revisar(self, v):
        print(v)


if __name__=='__main__':
    app = Principal()
    app.inicio()