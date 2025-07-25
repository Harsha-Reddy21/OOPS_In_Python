class Course:
    total_enrollments = 0
    
    def __init__(self, course_id, course_name, instructor, credits, max_capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits
        self.max_capacity = max_capacity
        self.enrolled_students = []
        self.waitlist = []
        self.grades = {}
    
    def __str__(self):
        return f"{self.course_id}: {self.course_name} by {self.instructor} ({self.credits} credits, {len(self.enrolled_students)}/{self.max_capacity} enrolled)"
    
    def get_available_spots(self):
        return self.max_capacity - len(self.enrolled_students)
    
    def get_enrollment_count(self):
        return len(self.enrolled_students)
    
    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity
    
    def enroll_student(self, student):
        if not self.is_full():
            if student.student_id not in self.enrolled_students:
                self.enrolled_students.append(student.student_id)
                Course.total_enrollments += 1
                return True
        else:
            if student.student_id not in self.waitlist:
                self.waitlist.append(student.student_id)
        return False
    
    def add_grade(self, student_id, grade):
        if student_id in self.enrolled_students:
            self.grades[student_id] = grade
    
    def get_course_stats(self):
        if not self.grades:
            return {"average": 0, "highest": 0, "lowest": 0, "count": 0}
        
        grades_list = list(self.grades.values())
        return {
            "average": sum(grades_list) / len(grades_list),
            "highest": max(grades_list),
            "lowest": min(grades_list),
            "count": len(grades_list)
        }
    
    @classmethod
    def get_total_enrollments(cls):
        return cls.total_enrollments


class Student:
    total_students = 0
    all_students = []
    
    def __init__(self, student_id, name, email, major):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.enrolled_courses = []
        self.grades = {}
        Student.total_students += 1
        Student.all_students.append(self)
    
    def __str__(self):
        return f"{self.student_id}: {self.name} ({self.email}) - {self.major}"
    
    def enroll_in_course(self, course):
        if course.course_id not in self.enrolled_courses:
            success = course.enroll_student(self)
            if success:
                self.enrolled_courses.append(course.course_id)
                return f"Successfully enrolled in {course.course_name}"
            else:
                return f"Added to waitlist for {course.course_name}"
        return f"Already enrolled in {course.course_name}"
    
    def add_grade(self, course_id, grade):
        if course_id in self.enrolled_courses:
            self.grades[course_id] = grade
    
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        
        total_points = 0
        total_credits = 0
        

        for grade in self.grades.values():
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
            else:
                total_points += 0.0
            total_credits += 1
        
        return total_points / total_credits if total_credits > 0 else 0.0
    
    def get_transcript(self):
        transcript = []
        for course_id, grade in self.grades.items():
            transcript.append(f"{course_id}: {grade}")
        return transcript
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    @classmethod
    def get_average_gpa(cls):
        if not cls.all_students:
            return 0.0
        
        total_gpa = sum(student.calculate_gpa() for student in cls.all_students)
        return total_gpa / len(cls.all_students)
    
    @classmethod
    def get_top_students(cls, count=2):
        sorted_students = sorted(cls.all_students, key=lambda s: s.calculate_gpa(), reverse=True)
        return [(student.name, student.calculate_gpa()) for student in sorted_students[:count]]



math_course = Course("MATH101", "Calculus I", "DR. Smith", 3, 30)
physics_course = Course("PHYS101", "Physics I", "DR. Johnson", 4, 25)
cs_course = Course("CS101", "Programming Basics", "DR. Brown", 3, 20)

print(f"Course info: {math_course}")
print(f"Available spots in Math: {math_course.get_available_spots()}")

student1 = Student("S001", "Alice Wilson", "alice@university.edu", "Computer Science")
student2 = Student("S002", "Bob Davis", "bob@university.edu", "Mathematics")
student3 = Student("S003", "Carol Lee", "carol@university.edu", "Physics")

print(f"Student: {student1}")
print(f"Total Students: {Student.get_total_students()}")

enrollment1 = student1.enroll_in_course(math_course)
enrollment2 = student1.enroll_in_course(cs_course)
enrollment3 = student2.enroll_in_course(math_course)

print(f"Alice's enrollment in Math: {enrollment1}")
print(f"Math course enrollment count: {math_course.get_enrollment_count()}")


student1.add_grade("MATH101", 85.5)
student1.add_grade("CS101", 92.0)
student2.add_grade("MATH101", 90.0)

print(f"Alice's GPA: {student1.calculate_gpa()}")
print(f"Alice's transcript: {student1.get_transcript()}")


math_course.add_grade("S001", 85.5)
math_course.add_grade("S002", 78.3)


course_stats = math_course.get_course_stats()
print(f"Math course stats: {course_stats}")


total_enrollments = Course.get_total_enrollments()
print(f"Total enrollments: {total_enrollments}")


average_gpa = Student.get_average_gpa()
print(f"Average GPA: {average_gpa}")


top_students = Student.get_top_students()
print(f"Top 2 students: {top_students}")


for i in range(25):
    temp_student = Student(f"S{i+100}", f"Student {i}", f"student{i}@uni.edu", "General")
    result = temp_student.enroll_in_course(math_course)

print(f"Course full status: {math_course.is_full()}")
print(f"Waitlist size: {len(math_course.waitlist) if math_course.is_full() else 0}")









