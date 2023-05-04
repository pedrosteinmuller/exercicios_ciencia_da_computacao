from abc import ABC, abstractmethod


class BancoStrategy(ABC):  # Interface
    @classmethod
    @abstractmethod
    def debitar(cls):
        raise NotImplementedError


class SantanderStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos específico do Santander (exemplo)
        print("Santander, Débito efetuado!")
