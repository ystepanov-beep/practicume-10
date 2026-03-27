cost_card = (input())


def calculate_card_value(card_cost: str) -> str:
    """Returns the card value including the bonus for valid card prices."""
    try:
        card_cost = int(card_cost)

        if card_cost == 5 or card_cost == 10:
            return str(card_cost)
        if card_cost == 25:
            return str(card_cost + 3)
        if card_cost == 50:
            return str(card_cost + 8)
        if card_cost == 100:
            return str(card_cost + 20)

        return "Отсутствуют предложения по этой цене"
    except ValueError:
        return "Некорректно введено значение"


print(calculate_card_value(cost_card))
