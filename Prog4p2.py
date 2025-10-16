from tkinter import *
from tkinter import messagebox

class Ventana():
    def __init__(self):
        self.ven = Tk()
        self.ven.title('Programa 1 con ventanas')
        self.ven.geometry('400x200')
        self.inicio()

    def inicio(self):
        Label(self.ven, text='Usuario').pack(pady=10)  
        self.us = Entry(self.ven)
        self.us.pack(pady=3)
        
        Label(self.ven, text='Password').pack(pady=10)  
        self.pas = Entry(self.ven, show='*')  
        self.pas.pack(pady=3)
        
        boton = Button(self.ven, text='Aceptar', command=self.revisar).pack(pady=3)  
        
        self.ven.mainloop()

    def revisar(self):
        try:
            u = str(self.us.get())
            p = str(self.pas.get())
            if u == 'admin' and p == '12345':
                messagebox.showinfo('Validacion', 'Usuario y contraseña correctos')
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrectos')
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos')

if __name__ == '__main__':
    app = Ventana()