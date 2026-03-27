def common_multiples_up_to_n(a: int, b: int, n: int) -> None:
    """Prints all common multiples of two numbers not greater than n."""

    result = []
    for i in range(n):
        if (i + 1) % a == 0 and (i + 1) % b == 0:
            result.append(i + 1)
    return result


a = int(input())
b = int(input())
n = int(input())
print(common_multiples_up_to_n(a, b, n))