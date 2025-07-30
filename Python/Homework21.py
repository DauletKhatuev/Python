#1 Задание
from collections import Counter
text = "Programming is fun!"
counter = Counter(text.lower())
print(counter)

#2 Задание
from collections import defaultdict

def group_students_by_class(students):
    class_dict = defaultdict(list)
    for class_num, name in students:  
        class_dict[class_num].append(name)
    return dict(class_dict)

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

result = group_students_by_class(students)
print("Классы и студенты:")
for class_num, names in result.items():
    print(f"{class_num}: {', '.join(names)}")
