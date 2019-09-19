from ed.lista_duplamente_ligada import ListaDuplamenteLigada


class ListaDeNodos(ListaDuplamenteLigada):

    def __init__(self):
        super().__init__()

    def imprimir(self, nivel):
        atual = self.inicio
        for i in range(0, self.quantidade):
            atual.conteudo.imprimir(nivel)
            atual = atual.proximo


class Nodo:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def __repr__(self):
        return self.conteudo

    def imprimir(self, nivel=0):
        print("{}- {}".format(" "*nivel, self.conteudo))
        if self.filhos:
            self.filhos.imprimir(nivel+1)

    def inserir_filho(self, filho):

        if self.filhos is None:
            self.filhos = ListaDeNodos()
        nodo = Nodo(filho)
        nodo.pai = self
        self.filhos.inserir_no_fim(nodo)


class Arvore:

    def __init__(self, conteudo):
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()
