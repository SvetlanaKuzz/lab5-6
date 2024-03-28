def z5_1():
    import random
    random_list = []
    for i in range(5):
        random_list.append(random.randint(1, 5))
    user_num = int(input("Введите число: "))
    if user_num in random_list:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

def z5_2():
    import random
    u_list = set() #множество под уникальные числа
    dup = set() #повторы
    random_list = []
    for i in range(5):
        random_list.append(random.randint(1, 5))
    for item in random_list: #проверка каждого элемента списка
        if item in u_list: #если элемент есть в множестве уникальных чисел
            dup.add(item) #оно попадает в список повторов
        else:
            u_list.add(item) #иначе добавляется в множество
    if dup: #если список не пустой
        print("Повторяющиеся элементы:", dup)
    else:
        print("Повторяющихся элементов нет")
    print(random_list)

def z5_3():
    days_of_the_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    num_weekend = int(input("Сколько выходных дней на неделе вы хотите?: "))
    split_i = len(days_of_the_week) - num_weekend #разделение дней
    weekend_days = days_of_the_week[split_i:] #списки выходных и рабочих дней
    work_days = days_of_the_week[:split_i]
    print("Ваши выходные дни:", weekend_days)
    print("Ваши рабочие дни:", work_days)

def z5_4():
    import random
    group_1 = ['Иванов', 'Орлов', 'Сидоров', 'Кузнецов', 'Зайцев']
    group_2 = ['Павлов', 'Иванов', 'Лебедев',  'Семенов', 'Васин']
    #1
    sport_team = tuple(random.sample(group_1, 2) + random.sample(group_2, 3))
    #2
    print("Группа 1:", group_1)
    print("Группа 2:", group_2)
    print("Спортивная команда:", sport_team)
    #3
    print("Длина кортежа:", len(sport_team))
    #4
    sorted_team = tuple(sorted(sport_team))
    print("Отсортированная команда:", sorted_team)
    #5
    if "Иванов" in sport_team:
        print("Студент Иванов в команде")
        print("Количество Ивановых в команде:", sport_team.count('Иванов'))
    else:
        print("Иванова нет в команде")

def z6_1():
    countries = {
    'Россия': 'Москва',
    'Великобритания': 'Лондон',
    'США': 'Вашингтон',
    'Германия': 'Берлин',
    'Франция': 'Париж'
    }
    #1
    for country, capital in countries.items(): #разделение ключа и значения
        print(country, "-", capital)
    #2
    country = input("Введите страну: ")
    print(f"Столица {country}: {countries[country]}")
    #3
    sorted_countries = sorted(countries.items())
    print("Содержимое словаря в алфавитном порядке:", sorted_countries)

def z6_2():
    scores = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
    }
    a = input("Введите слово: ").upper()
    total = 0
    for i in a:
        if i in scores:
            total = total + scores[i]
    print(f"Стоимость слова {a}: {total}")

def z6_22():
    scores = {
    1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['Й', 'Ы'],
    5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
    8: ['Ш', 'Э', 'Ю'],
    10: ['Ф', 'Щ', 'Ъ']
    }
    a = input("Введите слово: ").upper()
    total = 0
    for i in a:
        for number, word in scores.items():
            if i in word:
                total = total + number
    print(f"Стоимость слова {a}: {total}")


def z6_3():
    import random
    students = {}
    languages = ["английский", "французский", "немецкий", "испанский", "китайский", "итальянский"]
    ch_speakers = []
    n_students = random.randint(1, 5) #генерация случайного кол-ва студентов
    for i in range(n_students):
        student_lang = set(random.sample(languages, random.randint(1, len(languages)))) #множество с неповторяющимися языками
        students[f"Студент {i + 1}"] = student_lang #создание ключ-значений
    for student, langs in students.items(): #разделение ключ-значений
        print(student,":", langs) #вывод информации по каждому студенту
    #все уникальные языки, которые знают студенты
    all_lang = set()
    for langs in students.values(): #цикл со значениями
        all_lang.update(langs)
    print("Отсортированный список языков, которые знают студенты:", sorted(all_lang))
    #Вывод списка студентов, которые знают китайский язык
    for student, langs in students.items():
        if "китайский" in langs:
            ch_speakers.append(student)
    print("Студенты, знающие китайский язык:", ch_speakers)
z5_1()
z5_2()
z5_3()
z5_4()
z6_1()
z6_2()
z6_22()
z6_3()

