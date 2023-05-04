# criando uma lista de exemplo
minha_lista = [1, 2, 3, 4, 5]

# criando um objeto iterador a partir da lista usando a função iter()
meu_iterador = iter(minha_lista)

# verificando o tipo do iterador
print(type(meu_iterador))  # saída: <class 'list_iterator'>

print(next(meu_iterador))  # saída: 1
print(next(meu_iterador))  # saída: 2
print(next(meu_iterador))  # saída: 3
