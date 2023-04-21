class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo) -> None:
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self) -> str:
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 805)
    return 5 / n


try:
    division()
except MiError as e:
    print(e)
