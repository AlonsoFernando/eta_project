from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list: list):  #BUG - Transfomar flavors em lista
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        if len(self.flavors) > 0:
            msg = "No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                if flavor == self.flavors[-1]:
                    msg = f'{msg} {flavor}'
                    break
                msg = f'{msg} {flavor},'
            return msg
        else:
            return "Estamos sem estoque atualmente!"

        # BUG - Anterior -> Não entra no else pois é obrigado a passar algum valor para 'self.flavors'
        # MELHORIA - Criar lógica para entrar no if e, em caso de erro, no else
        # MELHORIA - Criar lógica de concatenação da mensagem de retorno positiva
        # MELHORIA - Substituir os prints por "return"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        if flavor in self.flavors:
            return f"Temos no momento {flavor}!"
        else:
            return f"Não temos no momento {flavor}!"

        # BUG - Estava retornando a lista inteira e não somente o item pesquisado
        # BUG - Não entra no else pois é obrigado a passar algum valor para flavors
        # MELHORIA - Substituir os prints por "return"
        # MELHORIA - RETIRADO o "(if self.flavors):" e "ELSE" para evitar duplicidade de retorno negativo

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if flavor in self.flavors:
            return "Sabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

        # BUG - Não entra no else pois é obrigado a passar algum valor para flavors
        # MELHORIA - Substituir os prints por "return"
        # MELHORIA - RetirADO o "(if self.flavors)" e "ELSE" pois a validação é apenas para a adição de sabores
