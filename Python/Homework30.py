from pathlib import Path
import json
from datetime import datetime
file_path = Path("C:/Users/vince/Desktop/ItCareerHub/Python/Materials/Homework30/student_courses.json")
students_per_course = {}
total_students = 0
courses_set = set()
courses = []
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
def parse_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y").date()
def calc_age(birth_date, enrollment_date):
    return enrollment_date.year - birth_date.year
course_counts = {}
total_age = 0
for i in data:
    birth_date = parse_date(i["birth_date"])
    enrollment_date = parse_date(i["enrollment_date"])
    total_students += 1

    for course in i["courses"]:
        if course not in course_counts:
            course_counts[course] = 0  # Инициализация перед увеличением
        course_counts[course] += 1

    age = calc_age(birth_date, enrollment_date)
    total_age += age
    average_age = total_age/total_students

print(total_students)
print(average_age)
print(course_counts)

