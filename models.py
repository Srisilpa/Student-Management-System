# models.py
class Student:
    def __init__(self, roll_no, name, branch, year, gender, age,
                 attendance, mid1, mid2, quiz, final):
        self.roll_no = int(roll_no)
        self.name = name
        self.branch = branch
        self.year = year
        self.gender = gender
        self.age = int(age)
        self.attendance = float(attendance)
        self.mid1 = float(mid1)
        self.mid2 = float(mid2)
        self.quiz = float(quiz)
        self.final = float(final)

    def to_dict(self):
        return {
            "Roll_No": self.roll_no,
            "Name": self.name,
            "Branch": self.branch,
            "Year": self.year,
            "Gender": self.gender,
            "Age": self.age,
            "Attendance_%": self.attendance,
            "Mid1_Marks": self.mid1,
            "Mid2_Marks": self.mid2,
            "Quiz_Marks": self.quiz,
            "Final_Marks": self.final,
        }
