


from tkinter import *
from tkinter import messagebox



def Ventana():
    def revisar():
        try:
            u = str(us.get())
            p = str(pas.get())
            if u == 'admin' and p == '12345':
                messagebox.showinfo('Validacion','Usuario y Contraseña Correctos')
            else:
                messagebox.showerror('Error','Usuario y/o contraseña incorrectos')
        except ValueError:
            messagebox.showerror('Error','Introduce datos')


    ven = Tk()
    ven.title('Programa 1 con ventanas')
    ven.geometry('400x200')
    Label(ven, text= 'Usuario').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=3)
    Label(ven, text='Password').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=13)
    boton = Button(ven, text='Aceptar', command=revisar).pack(pady=3)
    ven.mainloop()



if __name__== '__main__':
    Ventana()