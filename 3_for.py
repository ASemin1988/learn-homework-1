"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_students = [{'school_class': '1a', 'score': [3, 4, 4, 5, 2]},
                       {'school_class': '2a', 'score': [3, 4, 4, 5, 3]},
                       {'school_class': '3a', 'score': [3, 4, 4, 5, 5]},
                       {'school_class': '4a', 'score': [3, 4, 4, 5, 5]},
    ]

    test = []
    for klass_sum in school_students:
        klass = sum(klass_sum['score'])
        scores_avg1 = klass / len(klass_sum['score'])
        test.append(scores_avg1)
        print(f"Средняя оценка класса {scores_avg1}")
    test_sum = sum(test)
    sum_school = test_sum / len(test)
    print(sum_school)

if __name__ == "__main__":
    main()
