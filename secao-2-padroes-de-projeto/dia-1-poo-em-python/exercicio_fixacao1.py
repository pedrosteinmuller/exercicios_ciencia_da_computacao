class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    def cor(self):
        return self.__cor


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        if self.ventilador:
            return f"{self.nome} - possui um ventilador."
        return f"{self.nome} - não possui um ventilador."


ventilador_preto = Ventilador("preto", potencia=150, tensao=220, preco=80)
pessoa = Pessoa("Pedro", saldo_na_conta=10)
pessoa.comprar_ventilador(ventilador_preto)

print(pessoa)
