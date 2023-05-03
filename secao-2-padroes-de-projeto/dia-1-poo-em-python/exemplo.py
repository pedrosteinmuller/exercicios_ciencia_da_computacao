class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado


meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(
    cor="Vermelho", potencia=250, tensao=220, preco=100
)

liquidificador_vermelho = Liquidificador("Vermelho", 250, 220, 100)
liquidificador_vermelho.ligar(1)
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? True
liquidificador_vermelho.desligar()
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? False


# class Liquidificador:
#     # Getter
#     @property
#     def cor(self):
#         return self.__cor.upper()

#     @cor.setter # Repare que é @cor.setter, e não @property.setter
#     def cor(self, nova_cor):
#         if nova_cor.lower() == "turquesa":
#             raise ValueError("Não existe liquidificador turquesa")

#         self.__cor = nova_cor

#     def __init__(self, cor, potencia, tensao, preco):
#         # Observe que usamos o setter para já validarmos o primeiro valor:
#         # usamos self.cor, que chama o setter, e não self.__cor que manipula
#         # o atributo diretamente
#         self.cor = cor

#         # Demais variáveis omitidas para este exemplo


# liquidificador = Liquidificador("Rosa", "110", "127", "200")

# print(liquidificador.cor) # ROSA
# liquidificador.cor = "Vermelho"
# print(liquidificador.cor) # VERMELHO

class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador


pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)
