from modelos.alura import Restaurante

restaurante_1 = Restaurante('praça', 'gourmet')
restaurante_2 = Restaurante('mexican food', 'mexicano')
restaurante_3 = Restaurante('japa', 'japonesa')

restaurante_2.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()