studentScores = {
    "Harry": 85,
    "Hermione": 95,
    "Ron": 78,
    "Draco": 67,
    "Luna": 88,
    "Neville": 73,
    "Ginny": 90,
    "Fred": 82,
    "George": 82,
    "Cho": 66
}

studentGrades = {}

for score in studentScores:
    iScore = studentScores[score]
    if 91 <= iScore <= 100:
        grade = "Outstanding"
        studentGrades[score] = grade
    elif 81 <= iScore <= 90:
        grade = "Exceeds Expectations"
        studentGrades[score] = grade
    elif 71 <= iScore <= 80:
        grade = "Acceptable"
        studentGrades[score] = grade
    else:
        grade = "Fail"
        studentGrades[score] = grade

print(studentGrades)
