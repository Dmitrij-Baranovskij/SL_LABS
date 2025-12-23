import pickle

students = {
    "Иванов": {"Математика": 8, "Физика": 7, "Химия": 9, "История": 8, "Информатика": 9},
    "Петров": {"Математика": 7, "Физика": 8, "Химия": 7, "История": 8, "Информатика": 8},
    "Сидоров": {"Математика": 9, "Физика": 8, "Химия": 9, "История": 9, "Информатика": 8},
    "Козлов": {"Математика": 6, "Физика": 7, "Химия": 8, "История": 7, "Информатика": 7},
    "Смирнов": {"Математика": 10, "Физика": 9, "Химия": 10, "История": 9, "Информатика": 10},
    "Новиков": {"Математика": 5, "Физика": 6, "Химия": 6, "История": 5, "Информатика": 6},
    "Васильев": {"Математика": 8, "Физика": 9, "Химия": 8, "История": 9, "Информатика": 8}
}

print("=" * 60)
print("Список всех студентов и их баллов:")
print("=" * 60)
for student, grades in students.items():
    print(f"\n{student}:")
    for subject, grade in grades.items():
        print(f"  {subject}: {grade}")

print("\n" + "=" * 60)
print("Средний балл каждого студента:")
print("=" * 60)
averages = {}
for student, grades in students.items():
    avg = sum(grades.values()) / len(grades)
    averages[student] = avg
    print(f"{student}: {avg:.2f}")

best_student = max(averages, key=averages.get)
worst_student = min(averages, key=averages.get)

print("\n" + "=" * 60)
print("Студенты с максимальным и минимальным средним баллом:")
print("=" * 60)
print(f"Максимальный средний балл: {best_student} - {averages[best_student]:.2f}")
print(f"Минимальный средний балл: {worst_student} - {averages[worst_student]:.2f}")

math_grades = [grades["Математика"] for grades in students.values()]
math_average = sum(math_grades) / len(math_grades)

print("\n" + "=" * 60)
print(f"Средний балл по Математике: {math_average:.2f}")
print("=" * 60)

students_above_avg_math = {
    student: grades for student, grades in students.items() 
    if grades["Математика"] > math_average
}

print("\nСтуденты с оценкой по Математике выше среднего:")
print("=" * 60)
for student, grades in students_above_avg_math.items():
    print(f"{student}: Математика = {grades['Математика']} (выше среднего {math_average:.2f})")

with open('data.pickle', 'wb') as f:
    pickle.dump(students_above_avg_math, f)

print("\n" + "=" * 60)
print("Словарь студентов с оценкой по Математике выше среднего")
print("успешно сохранён в файл data.pickle")
print("=" * 60)

print("\nПроверка: загрузка данных из data.pickle")
print("=" * 60)
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print("Загруженные данные:")
    for student, grades in loaded_data.items():
        print(f"{student}: {grades}")
