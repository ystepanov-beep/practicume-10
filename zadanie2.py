n = int(input("Введите, сколько чисел Фибоначчи нужно вывести: "))


def fibonacci_numbers(n: int) -> None:
    """Prints the first n Fibonacci numbers."""
    first_number = 1
    second_number = 1
    fibonacci_numbers = []

    if n <= 0:
        print("Количество чисел должно быть больше нуля.")
        return

    if n == 1:
        fibonacci_numbers.append(first_number)
    else:
        fibonacci_numbers.append(first_number)
        fibonacci_numbers.append(second_number)

        for _ in range(n - 2):
            next_number = first_number + second_number
            fibonacci_numbers.append(next_number)
            first_number = second_number
            second_number = next_number

    return(fibonacci_numbers)


print(fibonacci_numbers(n))