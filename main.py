class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_student(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return round(mid_sum / len(self.grades.values()), 2)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grades_student() < other.average_grades_student()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grades_student() > other.average_grades_student()
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grades_student() == other.average_grades_student()
        else:
            return 'Ошибка'

    def __str__(self):
        self.courses_in_progress = self.courses_in_progress
        self.finished_courses = self.finished_courses
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades_student()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        average = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            average += course_mid
        if average == 0:
            return f'Оценок нет!'
        else:
            return round(average / len(self.grades.values()), 1)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades() < other.average_grades()
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades() > other.average_grades()
        else:
            return 'Ошибка'

    def __eq__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grades() == other.average_grades()
      else:
        return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grades()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя {self.name}\nФамилия {self.surname}'

student1 = Student("Иван", "Иванов", "М")
student2 = Student("Анна", "Петрова", "Ж")
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student2.courses_in_progress += ['Python', 'Git']
any_reviewer = Reviewer('Some', 'Buddy')
any_reviewer.courses_attached = ['Python', 'Git']
any_reviewer.rate_hw(student1, 'Python', 10)
any_reviewer.rate_hw(student1, 'Python', 8)
any_reviewer.rate_hw(student1, 'Git', 8)
any_reviewer.rate_hw(student1, 'Git', 7)
any_reviewer.rate_hw(student2, 'Python', 9)
any_reviewer.rate_hw(student2, 'Python', 10)
any_reviewer.rate_hw(student2, 'Git', 9)
any_reviewer.rate_hw(student2, 'Git', 6)
print(student1, student2, sep='\n')
print()
print(student1 < student2)
print(student1 > student2)
print(student1 == student2)
lecturer1 = Lecturer("Петя", "Маслов")
lecturer2 = Lecturer("Вася", "Пупкин")
lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Git']
student1.lecturer_grades('Python', 8, lecturer1)
student1.lecturer_grades('Python', 10, lecturer1)
student1.lecturer_grades('Python', 10, lecturer1)
student1.lecturer_grades('Python', 9, lecturer2)
student1.lecturer_grades('Python', 7, lecturer2)
student1.lecturer_grades('Python', 10, lecturer2)
print(lecturer1, lecturer2, sep='\n')
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 == lecturer2)
best_lecturer_1 = Lecturer('Dmitriy', 'Samardkanov')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Andrey', 'Chibisov')
best_lecturer_2.courses_attached += ['Java']
best_lecturer_3 = Lecturer('Vladimir', 'Filatov')
best_lecturer_3.courses_attached += ['Python']
student_1 = Student('Denis', 'Yatsenty', "M")
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
any_reviewer.rate_hw(student_1,'Python', 10)
any_reviewer.rate_hw(student_1,'Python', 7)

student_2 = Student('Roman', 'Li', "M")
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']
any_reviewer.rate_hw(student_2,'Python', 10)
any_reviewer.rate_hw(student_2,'Python', 3)
student_3 = Student('Alexey', 'Spitsin', "M")
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']
any_reviewer.rate_hw(student_3,'Python', 6)
any_reviewer.rate_hw(student_3,'Python', 2)
student_1.lecturer_grades(best_lecturer_1, 'Python', 10)
student_1.lecturer_grades(best_lecturer_1, 'Python', 10)
student_1.lecturer_grades(best_lecturer_1, 'Python', 10)
student_1.lecturer_grades(best_lecturer_2, 'Python', 5)
student_1.lecturer_grades(best_lecturer_2, 'Python', 7)
student_1.lecturer_grades(best_lecturer_2, 'Python', 8)
student_1.lecturer_grades(best_lecturer_1, 'Python', 7)
student_1.lecturer_grades(best_lecturer_1, 'Python', 8)
student_1.lecturer_grades(best_lecturer_1, 'Python', 9)
student_2.lecturer_grades(best_lecturer_2, 'Python', 10)
student_2.lecturer_grades(best_lecturer_2, 'Python', 8)
student_2.lecturer_grades(best_lecturer_2, 'Python', 9)
student_3.lecturer_grades(best_lecturer_3, 'Python', 5)
student_3.lecturer_grades(best_lecturer_3, 'Python', 6)
student_3.lecturer_grades(best_lecturer_3, 'Python', 7)
student_list_new = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
print(student_1, student_2, student_3, sep= '\n')

def all_student_rating(student_list, course_name):
    sum_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            for values in stud.grades.values():
                average_value = sum(values) / len(values)
                sum_all += average_value
               # print(average_value)
    return sum_all


def all_lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    for lecture in lecturer_list:
        if lecture.courses_attached == [course_name]:
            for values in lecture.grades.values():
                average_value = sum(values) / len(values)
                sum_all += average_value
            # print(average_value)
    return sum_all

average_student_all = all_student_rating(student_list_new,'Python')
average_lecture_all = all_lecturer_rating(lecturer_list,  'Python')
print(average_student_all, average_lecture_all, sep='\n')