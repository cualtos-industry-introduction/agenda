class Contacto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empresa = "Ninguna"
        self.correo = ""
        self.telefono = ""
        self.nota = ""

    def obtenerDatos(self):
        return self.__dict__
