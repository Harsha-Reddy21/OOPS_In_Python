from collections import defaultdict
class GradeManager:
    def __init__(self):
        self.grades = defaultdict(int)

    def add_grade(self,student_name,subject,grade):
        self.grades[student_name][subject].append(grade)

    def get_subject_statistics(self,subject):
        if not self.grades:
            return "No grades recorded yet"
        subject_grades = self.grades.values()
        if not subject_grades:
            return "No grades for this subject"
        return {
            "average":sum(subject_grades)/len(subject_grades),
            "highest":max(subject_grades),
            "lowest":min(subject_grades)
        }

    def get_top_students(self,n=3):
        if not self.grades:
            return "No grades recorded yet"
        student_scores = []
        for student,subjects in self.grades.items():
            if subject in subjects:
                student_scores.append(sum(subjects[subject])/len(subjects[subject]))
        return sorted(student_scores,reverse=True)[:n]

    def get_failing_students(self,passing_grade=50):
        if not self.grades:
            return "No grades recorded yet"
        failing_students = []
        for student,subjects in self.grades.items():
            if any(grade < passing_grade for grade in subjects.values()):
                failing_students.append(student)
        return failing_students

    def get_student_average(self,student_name):
        if not self.grades: 
            return "No grades recorded yet"
        if student_name not in self.grades:
            return "Student not found"
        return sum(self.grades[student_name].values())/len(self.grades[student_name])


manager = GradeManager()
grades_data=[
    ("Alice","Math",85),
    ("Alice","Science",90),
    ("Alice","History",78),
    ("Bob","Math",75),
    ("Bob","Science",82),
    ("Bob","History",88),
    ("Charlie","Math",92),
    ("Charlie","Science",88),
    ("Charlie","History",95),
    ("David","Math",70)
]

for student, subject, grade in grades_data:
    manager.add_grade(student,subject,grade)

print("Alice's average grade:",manager.get_student_average("Alice"))
print("Math subject statistics:",manager.get_subject_statistics("Math"))
print("Top 3 students:",manager.get_top_students())
print("Failing students:",manager.get_failing_students())







