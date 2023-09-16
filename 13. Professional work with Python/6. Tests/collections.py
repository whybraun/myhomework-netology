def get_unique_mentors(mentors: list):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        names = mentor.split()
        all_names_list.extend(names)

    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    result = (', '.join(all_names_sorted))

    return result


def get_top_3_names(mentors: list):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for men in all_list:
        name = (men.split(' ')[0])
        all_names_list.append(name)

    popular = []
    for name in all_names_list:
        popular.append((name, all_names_list.count(name)))

    popular.sort(key=lambda x: x[1], reverse=True)
    pop = sorted(set(popular), key=lambda x: x[1], reverse=True)

    top_3 = pop[:3]

    return top_3


def get_supernames_mentors(mentors: list, courses: list):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 != id2:
                intersection_set = set([
                    name for name in mentors_names[id1] if name in mentors_names[id2]])
                if len(intersection_set) > 0:
                    pair = list(intersection_set)
                    if pair not in pairs:
                        pairs.append(pair)
                        all_names_sorted = sorted(pair)
                        result = (f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
                        
    return result

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]