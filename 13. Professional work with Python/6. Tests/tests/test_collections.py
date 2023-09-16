from unittest import TestCase
from collections import mentors, courses, get_unique_mentors, get_top_3_names, get_supernames_mentors

class TestCollections(TestCase):

    def test_get_unique_mentors(self):
        result = get_unique_mentors(mentors)
        expected_result = 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Асканжоев, Бардин, Батицкая, Батырев, Беспоясов, Бибиков, Бочаров, Булыгин, Вадим, Валерий, Виролайнен, Владимир, Воронов, Воронцов, Глушков, Гордиенко, Грязнов, Демидов, Денис, Дерендяев, Дмитрий, Евгений, Ежков, Елена, Ерошевичев, Иван, Иванов, Илья, Индюков, Искаков, Кирилл, Константин, Коротков, Корсаков, Ларченко, Лопин, Максим, Маркитан, Михаил, Никита, Никитина, Николай, Нуруллин, Олег, Павел, Пеньков, Ринат, Роман, Сейсембаев, Сергей, Сердюк, Солонилин, Степанов, Сухачев, Табельский, Татьяна, Тен, Тимур, Ульянцев, Филипенко, Филипп, Фитискин, Хаслер, Чебукин, Шек, Шлейко, Шмаргунов, Шумский, Эдгар, Юрий, Юшина'
        self.assertEqual(result, expected_result)


    def test_get_top3_names(self):
        names = get_top_3_names(mentors)
        result = [name for name, _ in names]
        expected_name = 'Евгений'
        self.assertIn(expected_name, result)

    
    def test_get_supernames_mentors(self):
        result = get_supernames_mentors(mentors, courses)
        expected_course = 'Frontend-разработчик с нуля'
        self.assertIn(expected_course, result)





    
