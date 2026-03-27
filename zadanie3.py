purchase_amount_input = input("Введите стоимость покупки: ").strip()
has_discount_card = (
    input("Вы обладатель дисконтной карты?(да/нет): ").strip().lower() == "да"
)
is_holiday = (
    input("Сегодня праздничный день? (да/нет): ").strip().lower() == "да"
)


def discount_calculator(
        
    purchase_amount_input: str,
    has_discount_card: bool,
    is_holiday: bool,
) -> float:
    discount = 0
    """Calculates the final purchase price based on the purchase amount,
discount card, and holiday discount."""

    try:
        purchase_amount_input = purchase_amount_input.replace(",", ".")

        if "." not in purchase_amount_input:
            raise ValueError("Стоимость товара не должна быть целым числом.")

        decimal_part = purchase_amount_input.split(".")[1]

        if len(decimal_part) > 2:
            raise ValueError(
                "У числа не должно быть больше двух знаков после точки."
            )

        purchase_amount = float(purchase_amount_input)

        if is_holiday:
            discount += 3
        if has_discount_card:
            discount += 5
        if purchase_amount > 30000:
            discount += 10
        elif purchase_amount > 20000:
            discount += 7
        elif purchase_amount > 15000:
            discount += 5
        elif purchase_amount > 5000:
            discount += 3

        if discount > 15:
            discount = 15

        final_price = purchase_amount * (1 - discount / 100)
        return final_price

    except ValueError:
        print("Неверно введена стоимость покупки")
        return 0.0


final_price = discount_calculator(
    purchase_amount_input,
    has_discount_card,
    is_holiday,
)

print(f"Окончательная стоимость товара: {final_price:.2f}")
