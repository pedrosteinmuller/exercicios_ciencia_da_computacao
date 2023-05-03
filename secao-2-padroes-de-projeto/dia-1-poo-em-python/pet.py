# Visualizando dados de uma instância da classe por meio do método __str__


class Pet:
    def __init__(self, nome, especie, idade, humano):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.humano = humano

    def __str__(self):
        return (
            f"""
        - Espécie do pet: {self.especie}
        - Nome do pet: {self.nome}
        - Idade do pet: {self.idade}
        - Pessoa responsável: {self.humano}
        """
            ""
        )


titi = Pet("Tieres", "Cachorro", 4, "Pedro")

print(titi)
