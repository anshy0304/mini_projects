def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def generate_report_card(name, scores):
    report_card = {}
    total_subjects = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_subjects
    overall_grade = calculate_grade(average_score)

    report_card['Name'] = name
    report_card['Total Subjects'] = total_subjects
    report_card['Total Score'] = total_score
    report_card['Average Score'] = average_score
    report_card['Overall Grade'] = overall_grade

    return report_card

name = input("Enter student's name: ")
num_subjects = int(input("Enter the number of subjects: "))

scores = []
for i in range(1, num_subjects + 1):
    subject_score = float(input(f"Enter score for subject {i}: "))
    scores.append(subject_score)

report_card = generate_report_card(name, scores)

print("\nReport Card:")
for j, k in report_card.items():
    print(f"{j}: {k}")