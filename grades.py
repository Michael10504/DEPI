def calculate_average(grades):
    no = 0
    sum = 0
    for grade in grades:
        sum += grade
        no += 1
    return sum / no


def assign_grade(average):
    if average >= 94:
        return 'A'
    elif average >= 90:
        return 'A-'
    elif average >= 85:
        return 'B+'
    elif average >= 80:
        return 'B'
    elif average >= 75:
        return 'C+'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def get_student_summary(student_name, grades):
    x = calculate_average(grades)
    print("Average of grades of", student_name, "is", x)
    y = assign_grade(x)
    print("Letter grade of", student_name, "is", y)


def class_average(students):
    total = 0
    count = 0

    for grades in students:
        for grade in grades:
            total += grade
            count += 1
    return total / count
