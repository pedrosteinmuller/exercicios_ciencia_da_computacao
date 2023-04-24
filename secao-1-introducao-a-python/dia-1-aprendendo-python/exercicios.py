# exericio 1


def biggerNumber(number1, number2):
    if number2 > number1:
        return number2
    return number1


# exercicio 2


def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


# exercicio 3


def draw_square(n):
    for row in range(n):
        print(n * "*")


# exercicio 4


def find_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name
