import grades

def main():
    students = {
        "Ahmed": [90, 85, 88, 92],
        "Sara": [78, 82, 80, 75],
        "Omar": [95, 93, 97, 94]
    }

    print("Student Summaries")
 

    for name, grades_list in students.items():
        grades.get_student_summary(name, grades_list)
        print()

    all_grades = students.values()
    class_avg = grades.class_average(all_grades)

    print("Class Average:", class_avg)
    print("Class Letter Grade:", grades.assign_grade(class_avg))


if __name__ == "__main__":
    main()
