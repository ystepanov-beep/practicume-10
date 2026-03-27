P = input("Введите платеж по кредитной карте:")


def make_payment(P: str) -> str:
    """Returns the payment status for a credit card payment."""

    try:
        P = int(P)
        if P < 20 or P > 1000:
            return("Повторить попытку")
        else:
            return("Успех")
    except ValueError:
        return("Неверно введено значение")


print(make_payment(P))