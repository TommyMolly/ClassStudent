class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        return super().__str__()


class Reviewer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        return super().__str__()

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        completed_courses = ', '.join(self.finished_courses)
        in_progress_courses = ', '.join(self.courses_in_progress)
        avg_grade = self.calculate_avg_grade()

        return (f"{super().__str__()}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {in_progress_courses}\n"
                f"Завершенные курсы: {completed_courses}")

    def calculate_avg_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_tasks = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_tasks if total_tasks > 0 else 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return self.calculate_avg_lecture_grade() < other.calculate_avg_lecture_grade()

    def __le__(self, other):
        return self.calculate_avg_lecture_grade() <= other.calculate_avg_lecture_grade()

    def __gt__(self, other):
        return self.calculate_avg_lecture_grade() > other.calculate_avg_lecture_grade()

    def __ge__(self, other):
        return self.calculate_avg_lecture_grade() >= other.calculate_avg_lecture_grade()

    def calculate_avg_lecture_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_lectures = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_lectures if total_lectures > 0 else 0


student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Another', 'Student', 'female')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def calculate_avg_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_lectures = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_lectures if total_lectures > 0 else 0

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()


lecturer1 = Lecturer('Some', 'Lecturer1')
lecturer2 = Lecturer('Another', 'Lecturer2')

some_reviewer = Reviewer('Some', 'Reviewer1')
some_lecturer = Lecturer('Some', 'Lecturer1')
some_student = Student('Ruoy', 'Eman', 'male')

some_reviewer.courses_attached = ['Python']
some_lecturer.courses_attached = ['Python']
some_student.courses_in_progress += ['Python']

print(some_reviewer)
print(some_lecturer)
print(some_student)

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student2 = Student('Another', 'Student', 'female')
student2.courses_in_progress += ['Python', 'Git']

reviewer1 = Reviewer('Some', 'Reviewer1')
reviewer1.courses_attached = ['Python']
reviewer2 = Reviewer('Another', 'Reviewer2')
reviewer2.courses_attached = ['Python', 'Git']

lecturer1 = Lecturer('Some', 'Lecturer1')
lecturer1.courses_attached = ['Python']
lecturer2 = Lecturer('Another', 'Lecturer2')
lecturer2.courses_attached = ['Python', 'Git']


def avg_hw_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0


def avg_lecture_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grades / total_lecturers if total_lecturers > 0 else 0


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Git', 8)

python_students = [student1, student2]
python_lecturers = [lecturer1, lecturer2]

avg_hw = avg_hw_grade(python_students, 'Python')
avg_lecture = avg_lecture_grade(python_lecturers, 'Python')

print(f"Средняя оценка за домашние задания по курсу Python: {avg_hw:.2f}")
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture:.2f}")