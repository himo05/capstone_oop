class Student: # Crreate a student class
    def __init__(self, name, school_id, gpa): # These are its arguments
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self): # When the student is printed return this string
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'


def main(): # main function
    himo = Student('Himo', 'abcdef', 3.9)
    print(himo.name)
    print(himo.school_id)
    print(himo.gpa)
    print(himo)

main()