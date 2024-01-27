#hiii All THis is DAY84(27-01-2024) Today's is name and mark calculate result

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
  def get_total_marks(self):
    return sum(self.marks)
def main():
  students = []
  while True:
    name = input("Enter student name (or 'quit' to exit): ")
    if name == "quit":
      break
    marks = input("Enter student marks: ").split()
    marks = [int(mark) for mark in marks]
    student = Student(name, marks)
    students.append(student)
  for student in students:
    total_marks = student.get_total_marks()
    print(f"{student.name} total marks: {total_marks}")
if __name__ == "__main__":
  main()
