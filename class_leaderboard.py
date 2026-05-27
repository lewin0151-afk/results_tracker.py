#class_leaderboard
names = ["James Mwaura", "Lewin Kamau", "Claire Wambui", "Abdi Malik", "Lincon Smith"]
marks = [(50,90,10,70,98), (60,85,80,90,87), (80,90,50,45,69), (85,65,56,98,80), (50,90,99,50,80)]

def get_grade(average):
    if 75 <= average <= 100:
        return "A"
    elif 70 <= average <= 74:
        return "A-"
    elif 65 <= average <= 69:
        return "B+"
    elif 60 <= average <= 64:
        return "B"
    elif 55 <= average <= 59:
        return "B-"
    elif 50 <= average <= 54:
        return "C+"
    else:
        return "C"

results = []
for name, student_marks in zip(names, marks):
    average = sum(student_marks) / len(student_marks)
    grade = get_grade(average)
    results.append((name, round(average, 2), grade))

results.sort(key=lambda x: x[1], reverse=True) # sort by average

# Table
print("====CLASS RANKING====")
print(f"{'Pos':<7} {'Name':<12} {'Avg Points':<14} {'Grade'}")
print("-" * 35)

for rank, (name, avg, grade) in enumerate(results, start=1):
    print(f"{rank:<5} {name:<18} {avg:<11} {grade}")

print("-" * 35)
