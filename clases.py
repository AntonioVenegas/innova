class Producto():
    id = 0
    def __init__(self):
        id += 1
        self.id = id

class Etapa():
    id = 0
    def __init__(self):
        self.productos = []
        id += 1
        self.id = id

class Operacion(self, factor_emision=float):
    id = 0
    def __init__(self):
        self.etapas = []
        self.factor_emision = factor_emision
        id += 1
        self.id = id
    
    def add_etapa(self):
        pass

class Transporte():
    id = 0
    def __init__(self, insumo=Producto, factor_emision=float):
        self.insumo = insumo
        self.factor_emision = factor_emision
        id += 1
        self.id = id

class Proveedor():
    id = 0
    def __init__(self):
        self.transportes = []
        self.operaciones = []
        id += 1
        self.id = id

    def get_total_emitions(self):
        total = 0
        for t in self.transportes:
            total += t.factor_emision

        for o in self.operaciones:
            total += t.factor_emision



class Empresa():
    id = 0
    def __init__(self):
        pass