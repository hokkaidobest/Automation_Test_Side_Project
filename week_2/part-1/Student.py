class Student:
    # your code here

    def __init__(self):
        pass

    def set_student_details(self, student_name, mark1, mark2, mark3):
        self.student_name = student_name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_total(self):
        self.total_marks = self.mark1 + self.mark2 + self.mark3
        print(self.total_marks)

    def display_student_details(self):
        print(self.student_name, ":", self.total_marks)
        

student_a = Student()
student_a.set_student_details("Mary", 50, 60, 70)
student_a.calculate_total() # should print 180
student_a.display_student_details() # should print "Mary: 180"