import sys

class Student:
    def __init__(self, entrynum, name):
        self.entrynum = entrynum
        self.name = name
        self.current_courses = []  # List of Course objects

    def get_grade(marks):
    if marks >= 90: return 10
    elif marks >= 80: return 9
    elif marks >= 70: return 8
    elif marks >= 60: return 7
    elif marks >= 50: return 6
    elif marks >= 40: return 5
    elif marks >= 30: return 4
    else: return 0

    weighted_sum = 0
    total_credits = 0
    for i in sorted_courses:
        marks = i.registered_students[self.entrynum]
        if marks is not None:
            weighted_sum += get_grade(marks) * i.credits
            total_credits += i.credits
    
    cgpa = weighted_sum / total_credits if total_credits > 0 else 0
    handle.write(f"CGPA {int(cgpa)}\n")

    def generate_transcript(self):
        # TODO: Create a file named <name>_<entrynum>_transcript.txt
        handle = open(f'{self.name}_{self.entrynum}_transcript.txt','w')
        self.current_courses.sort(key=lambda course: course.coursecode)
        for i in self.current_courses:
            marks = i.registered_students[self.entrynum]
            handle.write(f"{i.coursecode} {marks}")
            if marks is not None:
                weighted_sum += get_grade(marks) * i.credits
                total_credits += i.credits

        cgpa = weighted_sum / total_credits if total_credits > 0 else 0
        handle.write(f"CGPA {int(cgpa)}\n")
        handle.close()
            

class Course:
    def __init__(self, coursecode, credits, capacity):
        self.coursecode = coursecode
        self.credits = credits
        self.capacity = capacity
        self.registered_students = {}  # entrynum -> marks

    def add_student(self, student_obj):
        # TODO: Handle capacity check and enrollment
        # Print error message to stdout if course is full
        if len(self.registered_students) == self.capacity:
            print(f"Course full. {student_obj.name} cannot enroll in {self.coursecode}.")
            
            
        else:
            self.registered_students[student_obj.entrynum] = None
            student_obj.current_courses.append(self)

    def remove_student(self, student_obj):
        # TODO: Remove student from the course if they are enrolled.
        if(student_obj.entrynum in self.registered_students):
            del self.registered_students[student_obj.entrynum]

    def load_marks(self):
        # TODO: Open <coursecode>_marks.txt and read marks
        # Read data in format: entrynum marks
        handle = open(f'{self.coursecode}_marks.txt', 'r')
        for i in handle:
           L = list(i.split())
           self.registered_students[L[0]] = int(L[1])
        handle.close()
        

class University:
    def __init__(self):
        self.students = {}  # entrynum -> Student
        self.courses = {}   # coursecode -> Course

    def process_commands(self):
        for line in sys.stdin:
            parts = line.strip().split()
            if not parts: continue

            cmd = parts[0]
            if cmd == 'COURSE':
                code, creds, cap = parts[1], int(parts[2]), int(parts[3])
                self.courses[code] = Course(code, creds, cap)
            elif cmd == 'ENROLL':
                entrynum, name = parts[1], parts[2]
                self.students[entrynum] = Student(entrynum, name)
            elif cmd == 'REGISTER':
                entrynum, code = parts[1], parts[2]
                self.courses[code].add_student(self.students[entrynum])
            elif cmd == 'DROP':
                entrynum, code = parts[1], parts[2]
                self.courses[code].remove_student(self.students[entrynum])
            elif cmd == 'MARKS':
                code = parts[1]
                self.courses[code].load_marks()
            elif cmd == 'TRANSCRIPT':
                entrynum = parts[1]
                self.students[entrynum].generate_transcript()

uni = University()
uni.process_commands()
