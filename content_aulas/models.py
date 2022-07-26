class Categoria:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.Categoria = categoria