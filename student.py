class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        total = 0
        for mark in self.marks:
            total += mark
        return total

    def minimum_marks(self):
        return min(self.marks)

    def maximum_marks(self):
        return max(self.marks)

    def average_of_marks(self):
        total = 0
        mark_len = len(self.marks)
        for mark in self.marks:
            total += mark
        average = total / mark_len
        return average

    def add_new_marks(self, new_mark):
        self.marks.append(new_mark)

    def remove_mark_at_index(self, index):
        del self.marks[index]


student = Student("Ranga", [23, 45, 56, 75])
number = student.get_number_of_marks()
sums = student.get_total_sum_of_marks()
min_number = student.minimum_marks()
max_number = student.maximum_marks()
average = student.average_of_marks()
print("Student[number-{}]".format(number))
print("Student[sum marks-{}]".format(sums))
print("Student[minimun number-{}]".format(min_number))
print("Student[maximum number-{}]".format(max_number))
print("Student[average number-{}]".format(average))
student.add_new_marks(55)
student.remove_mark_at_index(2)
print(student.marks)
