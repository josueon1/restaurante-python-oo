from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("praca","lanche")
cardapio_bebida=Bebida("suco de laranja",7.00,500)
cardapio_bebida.aplicar_desconto()
cardapio_prato=Prato("sanduba dahora",15.00,"moda da casa")
cardapio_prato.aplicar_desconto()


restaurante_praca.add_item_no_cardapio(cardapio_bebida)
restaurante_praca.add_item_no_cardapio(cardapio_prato)

def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()