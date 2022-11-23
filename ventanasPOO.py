# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/11/2022 09:25 am
# Última modificación: 23/11/2022 09:46 am
# Versión: 3.10.8

# Módulos importados
import tkinter as tk
from claseUsuario import *

# Fuentes widgets
fuente_label_titulos = ('bold italic', 30)
fuente_label_opciones_inst = ('bold italic', 14)
fuente_label_entry = ('Bold', 12)
fuente_label_botones = ('Bold', 14)
fuente_label_botones_submenu = ('Bold', 10)

# Clase ventanas
class Menu(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)
        self.config(bg='#323435')
        self.menu_principal(master) # Se introducen los widgets de menu_principal() dentro del Frame

    def menu_principal(self, master): 
        self.lBienvenida = tk.Label(self, text="¡Bienvenido a AeroTEC!", font=fuente_label_titulos,
                                bg='#323435', fg='white') # Se define el texto, fuente, color de fondo y letra
        self.lBienvenida.grid(column=0, row=0, columnspan=3) # Se define la ubicación del widget

        self.lInstruccion = tk.Label(self, text="Haga click en uno de los botones para realizar la acción que desee.",
                                 font=fuente_label_botones, bg='#323435', fg='white')
        self.lInstruccion.grid(column=0, row=1, columnspan=3)

        self.bImpProducto = tk.Button(self, text="1. Importar producto", font=fuente_label_botones, bg='#47494a',
                                        fg='white', activebackground='#f3f5f6', activeforeground='white',
                                        relief="groove", borderwidth=5, command=lambda: print(1)) # Los botones tendrán un color
                                                                                                  # casi blanco al ser presionados
        self.bImpProducto.grid(column=0, row=2, ipadx=15, ipady=15, padx=10, pady=10, columnspan=2)
        self.bImpProducto.config(width=20, height=1) # Medidas par que todos sean iguales
        
        self.bCrearUsuario = tk.Button(self, text="2. Crear usuarios", bg='#47494a', fg='white', font=fuente_label_botones,
                                   activebackground='#f3f5f6', activeforeground='white', relief="groove", borderwidth=5,
                                   command=lambda: print(2))
        self.bCrearUsuario.grid(column=1, row=2, ipadx=15, ipady=15, padx=10, pady=10, columnspan=2)
        self.bCrearUsuario.config(width=20, height=1)

        self.bGenerarCompras = tk.Button(self, text="3. Generar compras", bg='#646667', fg='white',
                                       font=fuente_label_botones, activebackground='#f3f5f6', activeforeground='white',
                                       relief="groove", borderwidth=5, command=lambda: print(3))
        self.bGenerarCompras.grid(column=0, row=3, ipadx=15, ipady=15, padx=10, pady=10)
        self.bGenerarCompras.config(width=20, height=1)

        self.bTracking = tk.Button(self, text="4. Tracking", bg='#646667', fg='white',
                               font=fuente_label_botones, relief="groove", borderwidth=5, activebackground='#f3f5f6',
                               activeforeground='white', command=lambda: print(4))
        self.bTracking.grid(column=1, row=3, ipadx=15, ipady=15, padx=10, pady=10)
        self.bTracking.config(width=20, height=1)

        self.bReportes = tk.Button(self, text="5. Reportes", bg='#646667', fg='white',
                                  font=fuente_label_botones, relief="groove", borderwidth=5, activebackground='#f3f5f6',
                                  activeforeground='white', command=lambda: print(5))
        self.bReportes.grid(column=2, row=3, ipadx=15, ipady=15, padx=10, pady=10)
        self.bReportes.config(width=20, height=1)

        self.bSalir = tk.Button(self, text="Salir", bg='#818384', fg='white',
                                    font=fuente_label_botones, relief="groove", borderwidth=5, activebackground='#f3f5f6',
                                    activeforeground='white', command=lambda: master.destroy())
        self.bSalir.grid(column=0, row=4, ipadx=15, ipady=15, padx=10, pady=10, columnspan=3)
        self.bSalir.config(width=20, height=1)
        

# Programa principal
ventana = tk.Tk()
app_aeroTec = Menu(master=ventana)
app_aeroTec.master.title('AeroTEC')
app_aeroTec.mainloop()