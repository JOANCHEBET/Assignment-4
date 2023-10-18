def calculate_grade(score):
    if score < 0 or score > 100:
        return 'invalid score'
    elif 0 <= score <= 30:
        return 'D'
    elif 31 <= score <= 50:
        return 'C'
    elif 51 <= score <= 70:
        return 'B'
    elif 71 <= score <= 100:
        return 'A'

def subject_score(subject_name):
    while True:
        try:
            score = float(input(f"Enter the {subject_name} score: "))
            return score
        except ValueError:
            print("Invalid input.")

math_score = subject_score("Math")
physics_score = subject_score("Physics")
geo_score = subject_score("Geography")
chem_score = subject_score("Chemistry")

average_score = (math_score + physics_score + geo_score + chem_score) / 4

if calculate_grade(average_score) == 'unrecognized marks/avg':
    print("Average grade: Unrecognized marks/avg")
else:
    print(f"Average grade: {calculate_grade(average_score)}")
