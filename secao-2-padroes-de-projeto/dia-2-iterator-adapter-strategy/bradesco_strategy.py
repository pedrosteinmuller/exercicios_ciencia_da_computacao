from abc import ABC, abstractmethod


class BancoStrategy(ABC):  # Interface
    @classmethod
    @abstractmethod
    def debitar(cls):
        raise NotImplementedError


class BradescoStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos específico do Bradesco (exemplo)
        print("Sucesso!")
