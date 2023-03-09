import statistics

students_list = []
lecturers_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def add_courses(self, course):
        self.finished_courses.append(course)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {statistics.mean(sum(self.grades.values(), []))} \n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.courses_in_progress))}\n" \
               f"Завершенные курсы: {', '.join(map(str, self.finished_courses))}"
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return statistics.mean(sum(self.grades.values(), [])) < statistics.mean(sum(other.grades.values(), []))
        else:
            return 'Ошибка'
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_list.append(self)
    
    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {statistics.mean(sum(self.grades.values(), []))} \n" \
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return statistics.mean(sum(self.grades.values(), [])) < statistics.mean(sum(other.grades.values(), []))
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'    
        
    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

def avg_grade_students(students_list, course):
    avg_grade = 0
    cnt = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            avg_grade += statistics.mean(sum(student.grades.values(), []))
            cnt += 1
    return round(avg_grade / cnt, 2)

def avg_grade_lecturers(lecturers_list, course):
    avg_grade = 0
    cnt = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            avg_grade += statistics.mean(sum(lecturer.grades.values(), []))
            cnt += 1
    return round(avg_grade / cnt, 2)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']
best_student.add_courses('Git')

bad_student = Student('Ettore', 'Siere', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['PHP']
bad_student.add_courses('Git')

cool_rewiewer = Reviewer('Some', 'Buddy')
cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.courses_attached += ['PHP']

cool_rewiewer = Reviewer('Peter', 'Hamington')
cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.courses_attached += ['PHP']
 
cool_rewiewer.rate_hw(best_student, 'Python', 4)
cool_rewiewer.rate_hw(best_student, 'Python', 5)
cool_rewiewer.rate_hw(best_student, 'Python', 5)
cool_rewiewer.rate_hw(best_student, 'PHP', 4)
cool_rewiewer.rate_hw(best_student, 'PHP', 5)
cool_rewiewer.rate_hw(best_student, 'PHP', 4)

cool_rewiewer.rate_hw(bad_student, 'Python', 3)
cool_rewiewer.rate_hw(bad_student, 'Python', 3)
cool_rewiewer.rate_hw(bad_student, 'Python', 4)
cool_rewiewer.rate_hw(bad_student, 'PHP', 3)
cool_rewiewer.rate_hw(bad_student, 'PHP', 5)
cool_rewiewer.rate_hw(bad_student, 'PHP', 3)

cool_lecturer = Lecturer('James', 'Bond')
cool_lecturer.courses_attached += ['Python']

super_lecturer = Lecturer('Merlyn', 'Monroe')
super_lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, "Python", 5)
best_student.rate_hw(cool_lecturer, "Python", 5)
best_student.rate_hw(cool_lecturer, "Python", 5)

bad_student.rate_hw(super_lecturer, "Python", 4)
bad_student.rate_hw(super_lecturer, "Python", 5)
bad_student.rate_hw(super_lecturer, "Python", 4)

print(best_student)
print(bad_student)
print(cool_rewiewer)
print(cool_lecturer)
print(super_lecturer)
print(best_student > bad_student)
print(super_lecturer > cool_lecturer)
print(avg_grade_students(students_list, 'Python'))
print(avg_grade_lecturers(lecturers_list, 'Python'))        