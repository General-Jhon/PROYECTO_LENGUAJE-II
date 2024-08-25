import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from Modelo.product import *
from Modelo.proveedor import *

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