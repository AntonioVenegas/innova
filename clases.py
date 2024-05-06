class Producto():
    id = 0
    def __init__(self):

class Etapa():
    id = 0
    def __init__(self):
        self.productos = []

class Operacion():
    id = 0
    def __init__(self):
        self.productos = []

class Transporte():
    id = 0
    def __init__(self):
        pass

class Proveedor():
    id = 0
    def __init__(self):
        self.transporte = []
        self.operaciones = []

class Empresa():
    id = 0
    def __init__(self):
        pass