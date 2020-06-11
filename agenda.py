import json

class Agenda():
    def __init__(self, nombre):
        self.contactos = []
        self.nombre = nombre
        self.archivo = nombre + '.tdb'
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo, 'r') as db:
                for registro in db:
                    print(registro)
                    contacto = json.loads(registro)
                    self.contactos.append(contacto)
        except FileNotFoundError as error:
            pass

    def guardar(self):
        with open(self.archivo, 'w') as db:
            for contacto in self.contactos:
                db.write(json.dumps(contacto))
                db.write('\n')

    def agregarContacto(self, contacto):
        if isinstance(contacto, dict):
            self.contactos.append(contacto)
        else:
            raise TypeError

    def mostrarContactos(self):
        return self.contactos

    def obtenerContacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                return contacto.copy()
            else:
                return {}
