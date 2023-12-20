# Created on Mon Jan 30 13:41:52 2023 by Chris Thompson
# Program to calculate average grade and determine letter grade

def calc_average_grade(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

# Determine the letter grade using conditional statements
def determine_letter_grade(average_grade):
    if average_grade >= 90:
        return "A"
    elif average_grade >= 80:
        return "B"
    elif average_grade >= 70:
        return "C"
    elif average_grade >= 60:
        return "D"
    else:
        return "F"

# Take input of three grades from the user
def main():
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))

    average_grade = calc_average_grade(grade1, grade2, grade3)
    letter_grade = determine_letter_grade(average_grade)
    
# Print the average grade and letter grade
    print(f"Average grade: {average_grade:.2f} ({letter_grade})")

if __name__ == "__main__":
    main()





