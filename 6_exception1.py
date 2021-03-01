"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_say = input('Как дела: ')
            word = 'Хорошо'
            if user_say == word:
                print('Я тоже думаю что хорошо')
                break
            else:
                print(f'Как твои дела {user_say}')
        except KeyboardInterrupt:
            print('\nПока')
            break

if __name__ == "__main__":
    hello_user()
