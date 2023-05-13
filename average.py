def average(numbers):
    """
    Функция, которая принимает список чисел и возвращает среднее значение.

    :param numbers: Список чисел.
    :return: Среднее значение.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)