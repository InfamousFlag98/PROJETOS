from modelos.alura import Restaurante

restaurante_1 = Restaurante('praça', 'gourmet')
restaurante_2 = Restaurante('mexican food', 'mexicano')
restaurante_3 = Restaurante('japa', 'japonesa')
restaurante_1.receber_avaliacao('Gui', 10)
restaurante_1.receber_avaliacao('Lais', 8)
restaurante_1.receber_avaliacao('Emy', 2)

restaurante_2.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()