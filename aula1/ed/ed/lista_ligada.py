class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaLigada:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def imprimir(self):
        celula_atual = self.inicio
        for i in range(0, self.quantidade):
            print(celula_atual.conteudo)
            celula_atual = celula_atual.proximo

    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1
