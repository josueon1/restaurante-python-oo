from modelos.restaurante import Restaurante

padaria=Restaurante('pao nosso','padaria')
padaria.receber_avaliacao('josue',10)
padaria.receber_avaliacao('julia',8)
padaria.receber_avaliacao('natana',8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()