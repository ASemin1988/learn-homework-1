"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_say = input('Как дела: ')
        word = 'Хорошо'
        if user_say == word:
            print('Я тоже думаю что хорошо')
            break
        else:
            print(f'Как твои дела {user_say}')

    
if __name__ == "__main__":
    hello_user()
