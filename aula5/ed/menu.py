from ed.arvore import Arvore


def main():

    livraria = Arvore("Livros")
    livraria.raiz.inserir_filho("Gastronomia")
    livraria.raiz.inserir_filho("Informática")
    livraria.imprimir()

    encontrado = livraria.localizar_nodo("Livros")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_nodo("Gastronomia")
    print("Encontrado: {}".format(encontrado))
    encontrado = livraria.localizar_nodo("Informática")
    print("Encontrado: {}".format(encontrado))

    encontrado = livraria.localizar_nodo("Turismo")
    print("Encontrado: {}".format(encontrado))

    livraria.inserir_nodo("Informática", "Linguagens")
    livraria.inserir_nodo("Linguagens", "Python")
    livraria.inserir_nodo("Gastronomia", "Culinária Brasileira")
    livraria.inserir_nodo("Gastronomia", "Bebidas")
    livraria.imprimir()

main()
