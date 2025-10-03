def validate_student(data):
    try:
        roll = int(data["Roll_No"])
        attendance = float(data["Attendance_%"])
        if not (0 <= attendance <= 100):
            return False, "Invalid attendance"
        for key in ["Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]:
            if float(data[key]) < 0 or float(data[key]) > 100:
                return False, f"Invalid {key}"
        return True, ""
    except Exception as e:
        return False, str(e)

def grade(total):
    if total >= 90: return "A"
    elif total >= 75: return "B"
    elif total >= 60: return "C"
    else: return "D"
