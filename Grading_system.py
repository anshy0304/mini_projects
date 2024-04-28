def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

score = float(input("Enter the score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    grade = calculate_grade(score)
    print(f"The grade for the score {score} is: {grade}")
