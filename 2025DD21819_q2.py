import sys

class Student:
    def __init__(self, entrynum, name):
        self.entrynum = entrynum
        self.name = name
        self.current_courses = []  # List of Course objects

    def generate_transcript(self):
        # TODO: Create a file named <name>_<entrynum>_transcript.txt
        open(f'{str(self.name)}_{str(self.entrynum)}_transcript.txt','w')

class Course:
    def __init__(self, coursecode, credits, capacity):
        self.coursecode = coursecode
        self.credits = credits
        self.capacity = capacity
        self.registered_students = {}  # entrynum -> marks

    def add_student(self, student_obj):
        # TODO: Handle capacity check and enrollment
        # Print error message to stdout if course is full
        if self.registered_students == self.capacity:
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
        handle = open(f'{self.coursecode}_tmarks.txt', 'r')
        for i in handle:
           L = list(i.split())
           self.registered_students[L[0]] = L[1]
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
