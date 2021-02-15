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
                       {'school_class': '3a', 'score': [3, 4, 4, 5, 5]}
    ]

    scores_sum = 0
    for score in school_students[0]['score']:
        scores_sum += score
    scores_avg1 = scores_sum / len(school_students[0]['score'])
    print(f"Средняя оценка класса '1а' {scores_avg1}")

    for score in school_students[1]['score']:
        scores_sum += score
    scores_avg2 = scores_sum / len(school_students[1]['score'])
    print(f"Средняя оценка класса '2а' {scores_avg2}")

    for score in school_students[2]['score']:
        scores_sum += score
    scores_avg3 = scores_sum / len(school_students[2]['score'])
    print(f"Средняя оценка класса '3а' {scores_avg3}")

    score_avg = 3
    scores_sum = scores_avg1 + scores_avg2 + scores_avg3
    scores_avg = scores_sum / score_avg
    print(f"Средняя оценка школы {scores_avg}")

if __name__ == "__main__":
    main()
