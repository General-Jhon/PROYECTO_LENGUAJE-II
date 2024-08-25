class Proveedor:
    def __init__(self, id_proveedor, nombre, direccion, telefono, correo):
        self.__id_proveedor = id_proveedor
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo

    @property
    def id_proveedor(self):
        return self.__id_proveedor

    @id_proveedor.setter
    def id_proveedor(self, id_proveedor):
        self.__id_proveedor = id_proveedor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        self.__correo = correo