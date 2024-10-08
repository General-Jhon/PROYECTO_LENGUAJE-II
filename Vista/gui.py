from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Controlador import *
from Modelo.product import Producto
from Modelo.proveedor import Proveedor
from Modelo.cliente import Cliente
from Modelo.orden import Orden
from Controlador.conexion import *
from Controlador.dao_logic import Dao

class MiVentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("880x670+300+200")
        self.root.title('Formulario Principal')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        #Imagen en Ventana
        self.img =PhotoImage(file='inventario.png')
        self.img_label=Label(self.root,image=self.img,border=0,bg='white')
        self.img_label.place(x=0,y=0)
        
        
        

        # Inicializar la conexión a la base de datos
        self.db = DataBase() 
        self.dao = Dao(self.db)  

        # Espacio para la barra de menú
        self.barraMenu = Menu(self.root)
        self.root.config(menu=self.barraMenu, width=600, height=600)

        # Menús dentro de la barra de menú
        self.cuentadanteMenu = Menu(self.barraMenu, tearoff=0)
        self.cuentadanteMenu.add_command(label='Administrar Productos', command=self.frm_producto)
        self.cuentadanteMenu.add_command(label='Administrar Proveedores', command=self.frm_proveedor)
        self.cuentadanteMenu.add_command(label='Administrar Clientes', command=self.frm_cliente)
        self.cuentadanteMenu.add_command(label='Administrar Órdenes', command=self.frm_orden)
        self.cuentadanteMenu.add_command(label='Salir', command=self.salir)

        self.ayudaMenu = Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu.add_command(label='Acerca de...')
        self.ayudaMenu.add_command(label='Licencia')

        # Agregar opciones a los menús
        self.barraMenu.add_cascade(label='Productos y Proveedores', menu=self.cuentadanteMenu)
        self.barraMenu.add_cascade(label='Ayuda', menu=self.ayudaMenu)
        
    
    def frm_cliente(self):
        # Ventana Cliente
        self.ventana_cliente = Toplevel(self.root)
        self.ventana_cliente.title('Administrar Clientes')
        self.ventana_cliente.geometry("800x600")

        Label(self.ventana_cliente, text="Cédula:").grid(row=0, column=0, padx=10, pady=10)
        self.ent_cedula = Entry(self.ventana_cliente, width=20, font=('Arial', 12))
        self.ent_cedula.grid(row=0, column=1)

        Label(self.ventana_cliente, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
        self.ent_nombre_cliente = Entry(self.ventana_cliente, width=20, font=('Arial', 12))
        self.ent_nombre_cliente.grid(row=1, column=1)

        Label(self.ventana_cliente, text="Dirección:").grid(row=2, column=0, padx=10, pady=10)
        self.ent_direccion_cliente = Entry(self.ventana_cliente, width=20, font=('Arial', 12))
        self.ent_direccion_cliente.grid(row=2, column=1)

        Label(self.ventana_cliente, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
        self.ent_telefono_cliente = Entry(self.ventana_cliente, width=20, font=('Arial', 12))
        self.ent_telefono_cliente.grid(row=3, column=1)

        Label(self.ventana_cliente, text="Correo:").grid(row=4, column=0, padx=10, pady=10)
        self.ent_correo_cliente = Entry(self.ventana_cliente, width=20, font=('Arial', 12))
        self.ent_correo_cliente.grid(row=4, column=1)

        Button(self.ventana_cliente, font=('Arial', 12, 'bold'), bg='blue', text="Guardar", command=self.guardar_cliente).grid(row=6, column=0, pady=5)
        Button(self.ventana_cliente, font=('Arial', 12, 'bold'), bg='orange', text="Actualizar", command=self.actualizar_cliente).grid(row=6, column=1, pady=5)
        Button(self.ventana_cliente, font=('Arial', 12, 'bold'), bg='red', text="Eliminar", command=self.eliminar_cliente).grid(row=6, column=2, padx=10, pady=5)
        Button(self.ventana_cliente, font=('Arial', 12, 'bold'), bg='green', text="Buscar", command=self.buscar_cliente).grid(row=7, column=1, padx=4, pady=5)

    def guardar_cliente(self):
        cliente = Cliente(
            cedula=self.ent_cedula.get(),
            nombre=self.ent_nombre_cliente.get(),
            direccion=self.ent_direccion_cliente.get(),
            telefono=self.ent_telefono_cliente.get(),
            correo=self.ent_correo_cliente.get()
        )
        self.dao.crear_cliente(cliente)

    def actualizar_cliente(self):
        cliente = Cliente(
            cedula=self.ent_cedula.get(),
            nombre=self.ent_nombre_cliente.get(),
            direccion=self.ent_direccion_cliente.get(),
            telefono=self.ent_telefono_cliente.get(),
            correo=self.ent_correo_cliente.get()
        )
        self.dao.actualizar_cliente(cliente)

    def eliminar_cliente(self):
        cedula = self.ent_cedula.get()
        self.dao.eliminar_cliente(cedula)

    def buscar_cliente(self):
        cedula_cliente = self.ent_cedula.get()
        cliente = self.dao.leer_cliente(cedula_cliente)
    
        if cliente:
            self.ent_nombre_cliente.delete(0, END)
            self.ent_nombre_cliente.insert(0, cliente.nombre)
            self.ent_direccion_cliente.delete(0, END)
            self.ent_direccion_cliente.insert(0, cliente.direccion)
            self.ent_telefono_cliente.delete(0, END)
            self.ent_telefono_cliente.insert(0, cliente.telefono)
            self.ent_correo_cliente.delete(0, END)
            self.ent_correo_cliente.insert(0, cliente.correo)

    def frm_producto(self):
        
        # Ventana Producto
        self.ventana_producto = Toplevel(self.root)
        self.ventana_producto.title('Administrar Productos')
        self.ventana_producto.geometry("800x600")
        

        # Añadir campos y botones para administrar productos
        Label(self.ventana_producto, text="ID Producto:").grid(row=0, column=0,padx=10,pady=10)
        self.ent_id_producto = Entry(self.ventana_producto,width=20,font=('Arial',12))
        self.ent_id_producto.grid(row=0, column=1)
        self.ent_id_producto.config(state='readonly')

        Label(self.ventana_producto, text="Nombre:").grid(row=1, column=0, padx=10,pady=10)
        self.ent_nombre = Entry(self.ventana_producto,width=20,font=('Arial',12))
        self.ent_nombre.grid(row=1, column=1)

        Label(self.ventana_producto, text="Descripción:").grid(row=2, column=0,padx=10,pady=10)
        self.ent_descripcion = Entry(self.ventana_producto,width=20,font=('Arial',12))
        self.ent_descripcion.grid(row=2, column=1)

        Label(self.ventana_producto, text="Precio:").grid(row=3, column=0,padx=10,pady=10)
        self.ent_precio = Entry(self.ventana_producto,width=20,font=('Arial',12))
        self.ent_precio.grid(row=3, column=1)

        Label(self.ventana_producto, text="Cantidad:").grid(row=4, column=0,padx=10,pady=10)
        self.ent_cantidad = Entry(self.ventana_producto,width=20,font=('Arial',12))
        self.ent_cantidad.grid(row=4, column=1)

        Button(self.ventana_producto,font=('Arial',12,'bold'),bg='blue',text="Guardar", command=self.guardar_producto).grid(row=6, column=0, pady=5)
        Button(self.ventana_producto,font=('Arial',12,'bold'),bg='orange',text="Actualizar", command=self.actualizar_producto).grid(row=6, column=1,pady=5)
        Button(self.ventana_producto,font=('Arial',12,'bold'),bg='red', text="Eliminar", command=self.eliminar_producto).grid(row=6, column=2,padx=10,pady=5)
        Button(self.ventana_producto, font=('Arial', 12, 'bold'), bg='green', text="Buscar", command=self.buscar_producto).grid(row=7, column=1,padx=4,pady=5)
    def frm_proveedor(self):
        
        
        #ventana proveedores
        self.ventana_proveedor = Toplevel(self.root)
        self.ventana_proveedor.title('Administrar Proveedores')
        self.ventana_proveedor.geometry("800x600")

        # Añadir campos y botones para administrar proveedores
        Label(self.ventana_proveedor, text="NIT Proveedor:").grid(row=0, column=0,padx=10,pady=10)
        self.ent_id_proveedor = Entry(self.ventana_proveedor,width=20,font=('Arial',12))
        self.ent_id_proveedor.grid(row=0, column=1)

        Label(self.ventana_proveedor, text="Nombre:").grid(row=1, column=0,padx=10,pady=10)
        self.ent_nombre_proveedor = Entry(self.ventana_proveedor,width=20,font=('Arial',12))
        self.ent_nombre_proveedor.grid(row=1, column=1)

        Label(self.ventana_proveedor, text="Dirección:").grid(row=2, column=0,padx=10,pady=10)
        self.ent_direccion = Entry(self.ventana_proveedor,width=20,font=('Arial',12))
        self.ent_direccion.grid(row=2, column=1)

        Label(self.ventana_proveedor, text="Teléfono:").grid(row=3, column=0,padx=10,pady=10)
        self.ent_telefono = Entry(self.ventana_proveedor,width=20,font=('Arial',12))
        self.ent_telefono.grid(row=3, column=1)

        Label(self.ventana_proveedor, text="Correo:").grid(row=4, column=0,padx=10,pady=10)
        self.ent_correo = Entry(self.ventana_proveedor,width=20,font=('Arial',12))
        self.ent_correo.grid(row=4, column=1)

        Button(self.ventana_proveedor,font=('Arial',12,'bold'),bg='blue', text="Guardar", command=self.guardar_proveedor).grid(row=6, column=0, pady=5)
        Button(self.ventana_proveedor,font=('Arial',12,'bold'),bg='orange', text="Actualizar", command=self.actualizar_proveedor).grid(row=6, column=1,pady=5)
        Button(self.ventana_proveedor,font=('Arial',12,'bold'),bg='red', text="Eliminar", command=self.eliminar_proveedor).grid(row=6, column=2,padx=10,pady=5)
        
        #Orden
    def frm_orden(self):
        self.ventana_orden = Toplevel(self.root)
        self.ventana_orden.title('Administrar Órdenes')
        self.ventana_orden.geometry("800x600")

    # Añadir campos y botones
        Label(self.ventana_orden, text="ID Orden:").grid(row=0, column=0, padx=10, pady=10)
        self.ent_id_orden = Entry(self.ventana_orden, width=20, font=('Arial', 12))
        self.ent_id_orden.grid(row=0, column=1)
        #self.ent_id_orden.config(state='readonly')

        Label(self.ventana_orden, text="Fecha:").grid(row=1, column=0, padx=10, pady=10)
        self.ent_fecha = Entry(self.ventana_orden, width=20, font=('Arial', 12))
        self.ent_fecha.grid(row=1, column=1)

        Label(self.ventana_orden, text="Cédula Cliente:").grid(row=2, column=0, padx=10, pady=10)
        self.ent_cedula_cliente = Entry(self.ventana_orden, width=20, font=('Arial', 12))
        self.ent_cedula_cliente.grid(row=2, column=1)

        Label(self.ventana_orden, text="Monto:").grid(row=3, column=0, padx=10, pady=10)
        self.ent_monto = Entry(self.ventana_orden, width=20, font=('Arial', 12))
        self.ent_monto.grid(row=3, column=1)

        Button(self.ventana_orden, font=('Arial', 12, 'bold'), bg='blue', text="Guardar", command=self.guardar_orden).grid(row=5, column=0, pady=5)
        Button(self.ventana_orden, font=('Arial', 12, 'bold'), bg='orange', text="Actualizar", command=self.actualizar_orden).grid(row=5, column=1, pady=5)
        Button(self.ventana_orden, font=('Arial', 12, 'bold'), bg='red', text="Eliminar", command=self.eliminar_orden).grid(row=5, column=2, padx=10, pady=5)
        Button(self.ventana_orden, font=('Arial', 12, 'bold'), bg='green', text="Buscar", command=self.buscar_orden).grid(row=5, column=3, padx=10, pady=5)

    def guardar_orden(self):
        orden = Orden(
            id_orden=self.ent_id_orden.get(),
            fecha=self.ent_fecha.get(),
            cedula_cliente=self.ent_cedula_cliente.get(),
            monto=float(self.ent_monto.get())
    )
        self.dao.crear_orden(orden)

    def actualizar_orden(self):
        orden = Orden(
            id_orden=self.ent_id_orden.get(),
            fecha=self.ent_fecha.get(),
            cedula_cliente=self.ent_cedula_cliente.get(),
            monto=float(self.ent_monto.get())
    )
        self.dao.actualizar_orden(orden)

    def eliminar_orden(self):
        id_orden = self.ent_id_orden.get()
        self.dao.eliminar_orden(id_orden)

    def buscar_orden(self):
        id_orden = self.ent_id_orden.get()
        orden = self.dao.leer_orden(id_orden)
    
        if orden:
            self.ent_fecha.delete(0, END)
            self.ent_fecha.insert(0, orden.fecha)
            self.ent_cedula_cliente.delete(0, END)
            self.ent_cedula_cliente.insert(0, orden.cedula_cliente)
            self.ent_monto.delete(0, END)
            self.ent_monto.insert(0, orden.monto)
  

    def guardar_producto(self):
        producto = Producto(
            id_producto=self.ent_id_producto.get(),
            nombre=self.ent_nombre.get(),
            descripcion=self.ent_descripcion.get(),
            precio=float(self.ent_precio.get()),
            cantidad=int(self.ent_cantidad.get())
        )
        self.dao.crear_producto(producto)

    def actualizar_producto(self):
        producto = Producto(
            id_producto=self.ent_id_producto.get(),
            nombre=self.ent_nombre.get(),
            descripcion=self.ent_descripcion.get(),
            precio=float(self.ent_precio.get()),
            cantidad=int(self.ent_cantidad.get())
        )
        self.dao.actualizar_producto(producto)

    def eliminar_producto(self):
        id_producto = self.ent_id_producto.get()
        self.dao.eliminar_producto(id_producto)
        
    def buscar_producto(self):
        nombre_producto = self.ent_nombre.get()
        producto = self.dao.buscar_producto_por_nombre(nombre_producto)
    
        if producto:
            self.ent_id_producto.config(state='normal')
            self.ent_id_producto.delete(0, END)
            self.ent_id_producto.insert(0, producto.id_producto)
            self.ent_id_producto.config(state='readonly')
            self.ent_nombre.delete(0, END)
            self.ent_nombre.insert(0, producto.nombre)
            self.ent_descripcion.delete(0, END)
            self.ent_descripcion.insert(0, producto.descripcion)
            self.ent_precio.delete(0, END)
            self.ent_precio.insert(0, producto.precio)
            self.ent_cantidad.delete(0, END)
            self.ent_cantidad.insert(0, producto.cantidad)



    def guardar_proveedor(self):
        proveedor = Proveedor(
            id_proveedor=self.ent_id_proveedor.get(),
            nombre=self.ent_nombre_proveedor.get(),
            direccion=self.ent_direccion.get(),
            telefono=self.ent_telefono.get(),
            correo=self.ent_correo.get()
        )
        self.dao.crear_proveedor(proveedor)
        
    def actualizar_proveedor(self):
        proveedor = Proveedor(
            id_proveedor=self.ent_id_proveedor.get(),
            nombre=self.ent_nombre_proveedor.get(),
            direccion=self.ent_direccion.get(),
            telefono=self.ent_telefono.get(),
            correo=self.ent_correo.get()
        )
        self.dao.actualizar_proveedor(proveedor)

    def eliminar_proveedor(self):
        id_proveedor = self.ent_id_proveedor.get()
        self.dao.eliminar_proveedor(id_proveedor)

    def salir(self):
        self.root.focus_set()
        rta = messagebox.askquestion('Salir', 'Desea salir de la aplicación?')
        if rta == 'yes':
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MiVentanaPrincipal(root)
    root.mainloop()