class Orden:
    def __init__(self, id_orden, fecha, cedula_cliente, monto):
        self.__id_orden = id_orden
        self.__fecha = fecha
        self.__cedula_cliente = cedula_cliente
        self.__monto = monto

    @property
    def id_orden(self):
        return self.__id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self.__id_orden = id_orden

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def cedula_cliente(self):
        return self.__cedula_cliente

    @cedula_cliente.setter
    def cedula_cliente(self, cedula_cliente):
        self.__cedula_cliente = cedula_cliente

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto = monto