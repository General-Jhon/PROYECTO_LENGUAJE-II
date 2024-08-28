import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from Modelo.product import *
from Modelo.proveedor import *
from Modelo.cliente import *
from Modelo.orden import *

class Dao:
    def __init__(self, database):
        self.db_connection = database.get_connection()
        self.cursor = self.db_connection.cursor()

    # CRUD Producto

    def crear_producto(self, producto: Producto):
        val = (producto.nombre, producto.descripcion, producto.precio, producto.cantidad)
        insert = 'insert into producto (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)'
        try:
            self.cursor.execute(insert, val)
            self.db_connection.commit()
            messagebox.showinfo('Nuevo Registro', 'El producto ha sido almacenado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def leer_producto(self, id_producto):
        query = 'SELECT * FROM producto WHERE id_producto = %s'
        try:
            self.cursor.execute(query, (id_producto,))
            result = self.cursor.fetchone()
            if result:
                return Producto(*result)
            else:
                messagebox.showinfo('No Encontrado', 'El producto no existe.')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def actualizar_producto(self, producto: Producto):
        update = 'UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s WHERE id_producto = %s'
        val = (producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.id_producto)
        try:
            self.cursor.execute(update, val)
            self.db_connection.commit()
            messagebox.showinfo('Actualización', 'El producto ha sido actualizado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def eliminar_producto(self, id_producto):
        delete = 'DELETE FROM producto WHERE id_producto = %s'
        try:
            self.cursor.execute(delete, (id_producto,))
            self.db_connection.commit()
            messagebox.showinfo('Eliminación', 'El producto ha sido eliminado...')
        except Error as e:
            messagebox.showerror('Error', str(e))
            
    def buscar_producto_por_nombre(self, nombre):
        query = 'SELECT * FROM producto WHERE nombre = %s'
        try:
            self.cursor.execute(query, (nombre,))
            result = self.cursor.fetchone()
            if result:
                return Producto(*result)
            else:
                return None
        except Error as e:
            messagebox.showerror('Error', str(e))
            return None

    # CRUD Proveedor

    def crear_proveedor(self, proveedor: Proveedor):
        val = (proveedor.nombre, proveedor.direccion, proveedor.telefono, proveedor.correo)
        insert = 'INSERT INTO proveedor (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)'
        try:
            self.cursor.execute(insert, val)
            self.db_connection.commit()
            messagebox.showinfo('Nuevo Registro', 'El proveedor ha sido almacenado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def leer_proveedor(self, id_proveedor):
        query = 'SELECT * FROM proveedor WHERE id_proveedor = %s'
        try:
            self.cursor.execute(query, (id_proveedor,))
            result = self.cursor.fetchone()
            if result:
                return Proveedor(*result)
            else:
                messagebox.showinfo('No Encontrado', 'El proveedor no existe.')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def actualizar_proveedor(self, proveedor: Proveedor):
        update = 'UPDATE proveedor SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id_proveedor = %s'
        val = (proveedor.nombre, proveedor.direccion, proveedor.telefono, proveedor.correo, proveedor.id_proveedor)
        try:
            self.cursor.execute(update, val)
            self.db_connection.commit()
            messagebox.showinfo('Actualización', 'El proveedor ha sido actualizado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def eliminar_proveedor(self, id_proveedor):
        delete = 'DELETE FROM proveedor WHERE id_proveedor = %s'
        try:
            self.cursor.execute(delete, (id_proveedor,))
            self.db_connection.commit()
            messagebox.showinfo('Eliminación', 'El proveedor ha sido eliminado...')
        except Error as e:
            messagebox.showerror('Error', str(e))
            
    #CRUD CLIENTE
    def crear_cliente(self, cliente: Cliente):
        val = (cliente.cedula, cliente.nombre, cliente.direccion, cliente.telefono, cliente.correo)
        insert = 'INSERT INTO cliente (cedula, nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(insert, val)
            self.db_connection.commit()
            messagebox.showinfo('Nuevo Registro', 'El cliente ha sido almacenado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def leer_cliente(self, cedula):
        query = 'SELECT * FROM cliente WHERE cedula = %s'
        try:
            self.cursor.execute(query, (cedula,))
            result = self.cursor.fetchone()
            if result:
                return Cliente(*result)
            else:
                messagebox.showinfo('No Encontrado', 'El cliente no existe.')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def actualizar_cliente(self, cliente: Cliente):
        update = 'UPDATE cliente SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE cedula = %s'
        val = (cliente.nombre, cliente.direccion, cliente.telefono, cliente.correo, cliente.cedula)
        try:
            self.cursor.execute(update, val)
            self.db_connection.commit()
            messagebox.showinfo('Actualización', 'El cliente ha sido actualizado...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def eliminar_cliente(self, cedula):
        delete = 'DELETE FROM cliente WHERE cedula = %s'
        try:
            self.cursor.execute(delete, (cedula,))
            self.db_connection.commit()
            messagebox.showinfo('Eliminación', 'El cliente ha sido eliminado...')
        except Error as e:
            messagebox.showerror('Error', str(e))
            
    #CRUD ORDEN
    def crear_orden(self, orden: Orden):
        val = (orden.fecha, orden.cedula_cliente, orden.monto)
        insert = 'INSERT INTO orden (fecha, cedula_cliente, monto) VALUES (%s, %s, %s)'
        try:
            self.cursor.execute(insert, val)
            self.db_connection.commit()
            messagebox.showinfo('Nuevo Registro', 'La orden ha sido almacenada...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def leer_orden(self, id_orden):
        query = 'SELECT * FROM orden WHERE id_orden = %s'
        try:
            self.cursor.execute(query, (id_orden,))
            result = self.cursor.fetchone()
            if result:
                return Orden(*result)
            else:
                messagebox.showinfo('No Encontrado', 'La orden no existe.')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def actualizar_orden(self, orden: Orden):
        update = 'UPDATE orden SET fecha = %s, cedula_cliente = %s, monto = %s WHERE id_orden = %s'
        val = (orden.fecha, orden.cedula_cliente, orden.monto, orden.id_orden)
        try:
            self.cursor.execute(update, val)
            self.db_connection.commit()
            messagebox.showinfo('Actualización', 'La orden ha sido actualizada...')
        except Error as e:
            messagebox.showerror('Error', str(e))

    def eliminar_orden(self, id_orden):
        delete = 'DELETE FROM orden WHERE id_orden = %s'
        try:
            self.cursor.execute(delete, (id_orden,))
            self.db_connection.commit()
            messagebox.showinfo('Eliminación', 'La orden ha sido eliminada...')
        except Error as e:
            messagebox.showerror('Error', str(e))