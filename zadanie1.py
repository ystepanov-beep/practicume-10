VOWELS = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
CONSONANTS = [
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
    'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
]

sentence = (
    "Функция принимает в качестве входных данных предложение на русском "
    "языке (строку) и печатает общее количество гласных и общее количество "
    "согласных букв в предложении. Функция не должна ничего возвращать. "
    "Обратите внимание, что предложение может иметь специальные символы, "
    "такие как точки, тире, и так далее."
)


def vowels_and_consonants_count(sentence: str) -> None:
    """Prints the number of vowels and consonants in a sentence"""
    vowels_count = 0
    consonants_count = 0

    for symbol in sentence:
        symbol = symbol.lower()
        if symbol in VOWELS:
            vowels_count += 1
        if symbol in CONSONANTS:
            consonants_count += 1

    return(f"Количество гласных: {vowels_count} \n"
    f"Количество согласных: {consonants_count}")


print(vowels_and_consonants_count(sentence))
