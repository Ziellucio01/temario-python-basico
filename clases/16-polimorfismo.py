

class Usuario():
    def guardar(self):
        print("guardado en la BBDD")


class Sesion():
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
# esto es poliformismo (crear metodos muy similares)
guardar([sesion, usuario])
