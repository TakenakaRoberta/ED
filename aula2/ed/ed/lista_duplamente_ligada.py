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

    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def inserir_no_inicio(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.proximo = self.inicio
        self._inicio.anterior = celula
        self._inicio = celula
        self._quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.anterior = self.fim
        self.fim.proximo = celula
        self._fim = celula
        self._quantidade += 1
