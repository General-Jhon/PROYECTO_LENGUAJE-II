import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_inventario_py'
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def get_connection(self):
        return self.connection

"""
class Dao:
    def __init__(self, database):
        self.connection = database.get_connection()
        self.cursor = self.connection.cursor()

    def obtener_productos(self):
        try:
            query = "SELECT * FROM Producto"  
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error al obtener los productos: {e}")

db = DataBase()
dao = Dao(db)
productos = dao.obtener_productos()
print(productos)
"""