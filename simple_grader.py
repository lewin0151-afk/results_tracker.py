#students_results_grader
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
       
def process_student(names,marks):
      total = sum(marks)
      average = total / len(marks)
      grade = get_grade(average)
      
      print("\n---STUDENT RESULTS ---")
      print("Names:",names)
      print("Marks:", marks)
      print("Total:",total)
      print("Average:",round(average, 5))
      print("Grade:",grade)
 
for i in range (len(names)):
    process_student(names[i], marks[i])
