class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class ListaDuplamenteLigada:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio
    @property
    def fim(self):
        return self._fim
    @property
    def quantidade(self):
        return self._quantidade

    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo
