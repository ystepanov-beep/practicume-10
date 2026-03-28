def allowed_numbers(A: int, B: int) -> list:
    """
    Creates and returns a list of numbers in the range [A, B]
    whose decimal representation contains at least one of
    the digits 1, 3, 4, 8, or 9.
    """

    set_of_numbers = {'1', '3', '4', '8', '9'}
    list_of_numbers = []

    if A > B:
        for i in range(B, A + 1):
            digits = set(str(i))
            if not digits.isdisjoint(set_of_numbers):
                list_of_numbers.append(i)
    else:
        for i in range(A, B + 1):
            digits = set(str(i))
            if not digits.isdisjoint(set_of_numbers):
                list_of_numbers.append(i)

    return list_of_numbers


A = int(input())
B = int(input())
print(allowed_numbers(A, B))
