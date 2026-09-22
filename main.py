print("====================================")
print("   STUDENT STUDY & RESULT MANAGER")
print("====================================")

print("\nWelcome to Student Study & Result Manager!")
print("Your study and result management system is ready.")

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.results = {}
        self.study = {}

    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)

    def calculate_average(self):
        if not self.results:
            return 0

        total = sum(self.results.values())
        subjects = len(self.results)

        return total / subjects

    def add_result(self, subject, marks):
        self.results[subject] = marks

    def add_study_session(self, subject, hours):
        self.study[subject] = hours

    def calculate_total_study_hours(self):
        return sum(self.study.values())

students = []


def add_student():
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    if not name or not roll_number:
        print("Name and roll number cannot be empty.")
        return

    for student in students:
        if student.roll_number == roll_number:
            print("A student with this roll number already exists.")
            return

    student = Student(name, roll_number)

    students.append(student)
    save_students()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENTS =====")

    for number, student in enumerate(students, start=1):
        print("Student:", number)
        student.display_info()
        print("--------------------")


def delete_student():
    roll_number = input("Enter roll number to delete: ").strip()

    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")


def search_student():
    search = input(
        "Enter student name or roll number: "
    ).strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    found = False

    for student in students:
        if (
            search in student.name.lower()
            or search == student.roll_number.lower()
        ):
            print("\n===== STUDENT FOUND =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)

            if student.results:
                print("Results:")
                for subject, marks in student.results.items():
                    print(subject, ":", marks)
            else:
                print("No results found.")

            print("--------------------")
            found = True

    if not found:
        print("Student not found.")


def update_student():
    roll_number = input("Enter roll number to update: ").strip()

    for student in students:
        if student.roll_number == roll_number:
            new_name = input("Enter new student name: ").strip()

            if not new_name:
                print("Name cannot be empty.")
                return

            student.name = new_name
            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def add_result():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            subject = input("Enter subject name: ").strip()

            if not subject:
                print("Subject name cannot be empty.")
                return

            marks = input("Enter marks: ").strip()

            if not marks.isdigit():
                print("Marks must be a number.")
                return

            marks = int(marks)

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            student.add_result(subject, marks)
            save_students()

            print("Result added successfully!")
            return

    print("Student not found.")


def update_result():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.results:
                print("No results found for this student.")
                return

            print("\nCurrent Results:")

            for subject, marks in student.results.items():
                print(subject, ":", marks)

            subject = input("Enter subject to update: ").strip()

            if subject not in student.results:
                print("Subject not found.")
                return

            marks = input("Enter new marks: ").strip()

            if not marks.isdigit():
                print("Marks must be a number.")
                return

            marks = int(marks)

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            student.results[subject] = marks
            save_students()

            print("Result updated successfully!")
            return

    print("Student not found.")


def delete_result():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.results:
                print("No results found for this student.")
                return

            print("\nCurrent Results:")

            for subject, marks in student.results.items():
                print(subject, ":", marks)

            subject = input("Enter subject to delete: ").strip()

            if subject not in student.results:
                print("Subject not found.")
                return

            del student.results[subject]
            save_students()

            print("Result deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.results:
                print("No results found for this student.")
                return

            total = sum(student.results.values())
            subjects = len(student.results)
            average = total / subjects

            print("\n===== RESULT AVERAGE =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)
            print("Average Marks:", round(average, 2))

            return

    print("Student not found.")


def calculate_grade():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.results:
                print("No results found for this student.")
                return

            total = sum(student.results.values())
            subjects = len(student.results)
            average = total / subjects

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\n===== STUDENT GRADE =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)
            print("Average Marks:", round(average, 2))
            print("Grade:", grade)

            return

    print("Student not found.")


def performance_summary():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.results:
                print("No results found for this student.")
                return

            total_marks = sum(student.results.values())
            total_subjects = len(student.results)
            average_marks = total_marks / total_subjects
            highest_marks = max(student.results.values())
            lowest_marks = min(student.results.values())

            print("\n===== PERFORMANCE SUMMARY =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)
            print("Total Subjects:", total_subjects)
            print("Total Marks:", total_marks)
            print("Average Marks:", round(average_marks, 2))
            print("Highest Marks:", highest_marks)
            print("Lowest Marks:", lowest_marks)

            return

    print("Student not found.")


def compare_students():
    roll_number1 = input("Enter first student roll number: ").strip()
    roll_number2 = input("Enter second student roll number: ").strip()

    student1 = None
    student2 = None

    for student in students:
        if student.roll_number == roll_number1:
            student1 = student

        if student.roll_number == roll_number2:
            student2 = student

    if student1 is None or student2 is None:
        print("One or both students not found.")
        return

    if not student1.results or not student2.results:
        print("Both students must have results.")
        return

    average1 = student1.calculate_average()
    average2 = student2.calculate_average()

    difference = abs(average1 - average2)

    print("\n===== STUDENT PERFORMANCE COMPARISON =====")
    print("Student 1:", student1.name)
    print("Average Marks:", round(average1, 2))

    print("--------------------")

    print("Student 2:", student2.name)
    print("Average Marks:", round(average2, 2))

    print("--------------------")
    print("Difference:", round(difference, 2), "marks")


def class_performance_summary():
    students_with_results = []

    for student in students:
        if student.results:
            students_with_results.append(student)

    if not students_with_results:
        print("No student results found.")
        return

    all_marks = []

    for student in students_with_results:
        for marks in student.results.values():
            all_marks.append(marks)

    total_students = len(students_with_results)
    total_records = len(all_marks)
    overall_average = sum(all_marks) / total_records
    highest_marks = max(all_marks)
    lowest_marks = min(all_marks)

    print("\n===== CLASS PERFORMANCE SUMMARY =====")
    print("Students with Results:", total_students)
    print("Total Result Records:", total_records)
    print("Overall Average Marks:", round(overall_average, 2))
    print("Highest Marks:", highest_marks)
    print("Lowest Marks:", lowest_marks)


def view_results():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            print("\n===== STUDENT RESULTS =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)

            if not student.results:
                print("No results found.")
                return

            print("--------------------")

            for subject, marks in student.results.items():
                print(subject, ":", marks)

            return

    print("Student not found.")


def add_study_session():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            subject = input("Enter subject name: ").strip()

            if not subject:
                print("Subject name cannot be empty.")
                return

            hours = input("Enter study hours: ").strip()

            try:
                hours = float(hours)
            except ValueError:
                print("Study hours must be a number.")
                return

            if hours <= 0:
                print("Study hours must be greater than 0.")
                return

            student.add_study_session(subject, hours)
            save_students()

            print("Study session added successfully!")
            return

    print("Student not found.")


def view_study_sessions():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            print("\n===== STUDY SESSIONS =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)

            if not student.study:
                print("No study sessions found.")
                return

            print("--------------------")

            for subject, hours in student.study.items():
                print(subject, ":", hours, "hours")

            return

    print("Student not found.")


def delete_study_session():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.study:
                print("No study sessions found.")
                return

            print("\nCurrent Study Sessions:")

            for subject, hours in student.study.items():
                print(subject, ":", hours, "hours")

            subject = input("Enter subject to delete: ").strip()

            if subject not in student.study:
                print("Subject not found.")
                return

            del student.study[subject]
            save_students()

            print("Study session deleted successfully!")
            return

    print("Student not found.")


def update_study_session():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.study:
                print("No study sessions found.")
                return

            print("\nCurrent Study Sessions:")

            for subject, hours in student.study.items():
                print(subject, ":", hours, "hours")

            subject = input("Enter subject to update: ").strip()

            if subject not in student.study:
                print("Subject not found.")
                return

            hours = input("Enter new study hours: ").strip()

            try:
                hours = float(hours)
            except ValueError:
                print("Study hours must be a number.")
                return

            if hours <= 0:
                print("Study hours must be greater than 0.")
                return

            student.study[subject] = hours
            save_students()

            print("Study session updated successfully!")
            return

    print("Student not found.")


def calculate_total_study_hours():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.study:
                print("No study sessions found.")
                return

            total_hours = sum(student.study.values())

            print("\n===== TOTAL STUDY HOURS =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)
            print("Total Study Hours:", total_hours)

            return

    print("Student not found.")


def study_progress_summary():
    roll_number = input("Enter student roll number: ").strip()

    for student in students:
        if student.roll_number == roll_number:

            if not student.study:
                print("No study sessions found.")
                return

            print("\n===== STUDY PROGRESS SUMMARY =====")
            print("Name:", student.name)
            print("Roll Number:", student.roll_number)
            print("--------------------")

            total_hours = sum(student.study.values())
            subjects = len(student.study)
            average_hours = total_hours / subjects

            for subject, hours in student.study.items():
                print(subject, ":", hours, "hours")

            print("--------------------")
            print("Total Study Hours:", total_hours)
            print("Average Study Hours:", round(average_hours, 2))

            return

    print("Student not found.")


def save_students():
    file = open("students.txt", "w")

    for student in students:
        results = ""
        study = ""

        for subject, marks in student.results.items():
            results += subject + ":" + str(marks) + ","

        for subject, hours in student.study.items():
            study += subject + ":" + str(hours) + ","

        file.write(
            student.name + "|"
            + student.roll_number + "|"
            + results + "|"
            + study + "\n"
        )

    file.close()


def load_students():
    try:
        file = open("students.txt", "r")

        for line in file:
            line = line.strip()

            if line:
                parts = line.split("|")

                if len(parts) < 2:
                    continue

                name = parts[0]
                roll_number = parts[1]

                student = Student(name, roll_number)

                if len(parts) >= 3 and parts[2]:
                    result_list = parts[2].split(",")

                    for result in result_list:
                        if ":" in result:
                            subject, marks = result.split(":")
                            student.results[subject] = int(marks)

                if len(parts) >= 4 and parts[3]:
                    study_list = parts[3].split(",")

                    for session in study_list:
                        if ":" in session:
                            subject, hours = session.split(":")
                            student.study[subject] = float(hours)

                students.append(student)

        file.close()

    except FileNotFoundError:
        pass


load_students()


while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Students")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Add Result")
    print("7. Update Result")
    print("8. Delete Result")
    print("9. View Results")
    print("10. Calculate Average")
    print("11. Calculate Grade")
    print("12. Performance Summary")
    print("13. Compare Students")
    print("14. Class Performance Summary")
    print("15. Study Tracker")
    print("16. Exit")

    choice = input("\nEnter your choice: ").strip()
    
    if not choice:
        print("Choice cannot be empty.")
        continue

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        add_result()

    elif choice == "7":
        update_result()

    elif choice == "8":
        delete_result()

    elif choice == "9":
        view_results()

    elif choice == "10":
        calculate_average()

    elif choice == "11":
        calculate_grade()

    elif choice == "12":
        performance_summary()

    elif choice == "13":
        compare_students()

    elif choice == "14":
        class_performance_summary()

    elif choice == "15":
        print("\n1. Add Study Session")
        print("2. View Study Sessions")
        print("3. Delete Study Session")
        print("4. Update Study Session")
        print("5. Calculate Total Study Hours")
        print("6. Study Progress Summary")

        study_choice = input("Enter your choice: ").strip()

        if not study_choice:
            print("Studychoice cannot be empty.")
            continue

        if study_choice == "1":
            add_study_session()

        elif study_choice == "2":
            view_study_sessions()

        elif study_choice == "3":
            delete_study_session()

        elif study_choice == "4":
            update_study_session()

        elif study_choice == "5":
            calculate_total_study_hours()

        elif study_choice == "6":
            study_progress_summary()

        else:
            print("Invalid choice.")

    elif choice == "16":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        