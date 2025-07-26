# Python Grade Calculator Program

def main():
    
    student_grades = []
    total = 0
    
    for i in range (5):
        grade = float(input(f"Enter grade #{i+1}: "))
        student_grades.append(grade)
        total += grade
        
    average = total / 5
    
    maximum = max(student_grades)
    minimum = min(student_grades)
    
    print(f"Average grade: {average}")
    print(f"Maximum grade: {maximum}")
    print(f"Minimum grade: {minimum}")
    
if __name__ == "__main__":
    main()
