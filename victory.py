import random

new_list = [
    {'actress': 'Джессики Честейн', 'date': '24.03.1977', 'another_date': '24 марта 1977г'},
    {'actress': 'Блейк Лавли', 'date': '25.08.1987', 'another_date': '25 августа 1987г'},
    {'actress': 'Софи Тернер', 'date': '21.02.1996', 'another_date': '21 февраля 1996г'},
    {'actress': 'Эмилии Кларк', 'date': '23.10.1986', 'another_date': '23 октября 1986г.'},
    {'actress': 'Дженнифер Лоуренс', 'date': '15.08.1990', 'another_date': '15 августа 1990г'},
    {'actress': 'Эммы Уотсон', 'date': '15.04.1990', 'another_date': '15 апреля 1990г'},
    {'actress': 'Дженнифер Лопес', 'date': '24.07.1969', 'another_date': '24 июля 1969г'},
    {'actress': 'Анджелины Джоли', 'date': '04.06.1957', 'another_date': '4 июня 1957г'},
    {'actress': 'Камерон Диас', 'date': '30.08.1972', 'another_date': '30 августа 1972'},
    {'actress': 'Дженифер Энистон', 'date': '11.02.1969', 'another_date': '11 февраля 1969г'}
]

result = random.sample(new_list, 5)

right_answers = 0

while True:
    for actress in result:
        answer = input(f'Введите день рождение {actress["actress"]} в формате дд.мм.гггг: ')
        if answer == actress['date']:
            print('Верно!')
            right_answers += 1
        else:
            print(f'Неверно, правильный ответ: {actress["another_date"]}')
    wrong_answers = 5 - right_answers
    print(f'Правильных ответов: {right_answers}')
    print(f'Неправильных ответов: {wrong_answers}')
    right_answers = 0
    wrong_answers = 5 - right_answers
    continue_again = input('Хотите продолжить? (да/нет)')
    if continue_again == 'нет':
        break
