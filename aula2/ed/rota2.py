from ed.lista_duplamente_ligada import ListaDuplamenteLigada, Celula


class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return " * {} - {}".format(self.nome, self.endereco)


def situacao(lista):
    print("Quantidade: {}".format(lista.quantidade))
    lista.imprimir()


def main():
    loja1 = Loja("Minimercardo", "Rua das Flores, 12")
    loja2 = Loja("Hortifruti", "Av das Borboletas, 23")
    loja3 = Loja("Padaria Pão Quente", "Praça da Árvore")
    loja4 = Loja("Supermercado", "Rua do Pomar, 23")
    loja5 = Loja("Mercado", "Rua das Flores, 98")
    loja6 = Loja("Quitanda", "Rua da Fazenda, 899")
    loja7 = Loja("Minimercardo das Frutas", "Av do Bosque, 66")
    loja8 = Loja("Supermercado das Frutas", "Rua do Pomar, 600")
    loja9 = Loja("Hortifruti da terra", "Rua das Laranjeira, 800")
    loja10 = Loja("Mercado do Campo", "Rua da Fazenda, 1500")

    lista = ListaDuplamenteLigada()
    lista._inserir_em_lista_vazia(loja1)
    situacao(lista)
































main()
