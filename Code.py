"""
Конвертер массы - преобразует между разными единицами измерения массы.
Поддерживает: тонны, центнеры, килограммы, граммы, миллиграммы.
"""


def convert_mass(value, from_unit, to_unit):
    """
    Конвертирует массу из одной единицы в другую.

    Аргументы:
        value: float - значение для конвертации
        from_unit: str - входная единица
        to_unit: str - выходная единица

    Возвращает:
        float - сконвертированное значение
    """
    # Коэффициенты перевода в килограммы
    to_kg = {
        'ton': 1000.0,      # тонна
        'quintal': 100.0,   # центнер
        'kg': 1.0,          # килограмм
        'gram': 0.001,      # грамм
        'mg': 0.000001      # миллиграмм
    }

    # Сначала переводим в килограммы, затем в выходную единицу
    kg_value = value * to_kg[from_unit]
    result = kg_value / to_kg[to_unit]

    return result


def display_units():
    """Показывает доступные единицы измерения пользователю."""
    print("\nДоступные единицы массы:")
    print("  - ton (тонна)")
    print("  - quintal (центнер)")
    print("  - kg (килограмм)")
    print("  - gram (грамм)")
    print("  - mg (миллиграмм)")


def get_user_input():
    """Получает от пользователя параметры конвертации."""
    print("=== Конвертер массы ===")
    display_units()

    value = float(input("\nВведите значение для конвертации: "))
    from_unit = input("Введите входную единицу: ").strip().lower()
    to_unit = input("Введите выходную единицу: ").strip().lower()

    return value, from_unit, to_unit


def main():
    """Главный цикл программы."""
    try:
        value, from_unit, to_unit = get_user_input()
        result = convert_mass(value, from_unit, to_unit)

        print(f"\nРезультат: {value} {from_unit} = {result} {to_unit}")

    except KeyError:
        print("\nОшибка: Неверная единица измерения!")
    except ValueError:
        print("\nОшибка: Неверное число!")
    except ZeroDivisionError:
        print("\nОшибка: Невозможно конвертировать!")


if __name__ == "__main__":
    main()
