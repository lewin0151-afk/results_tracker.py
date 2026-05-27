#class_ranking
names= ["James", "Lewin","Alice","sharon","Lincon"]
marks= [(50,90,70,98),(60,55,90,87),(80,90,45,69),(85,55,98,80),(50,90,99,80)]

def get_grade(average):
    if 75 <= average <=100:
        return "A"
    elif 70 <= average < 74:
        return "A-"
    elif 65 <= average < 69:
        return "B+"
    elif 60 <= average < 64:
       return "B"
    elif 55 <= average < 59:
       return "B-"
    elif 50 <= average < 54:
       return "C+"
    else:
           return "C"
results = []

for name, student_marks in zip(names, marks):
    total = sum(student_marks)
    average = total/len(student_marks)
    grade = get_grade(average)
    results.append((name, student_marks,total,round(average, 5), grade))
    
results.sort(key=lambda x: x[3], reverse = True)
   
print("====CLASS RANKING====")
for rank,(name, student_marks, total, average,grade) in enumerate(results, start= 1):
        print(f"\n{rank},{name}")
        print(f"Marks:{student_marks}")
        print(f"Total:{total} | Average:{average} |Grade : {grade}")
