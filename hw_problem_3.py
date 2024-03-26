# HW1_P3: The Grade Analyzer

grades = [80, 90, 50, 88, 95, 78, 81]

# Task 1: Code a function to calculate the average grade.

def calc_avg(grades):
    total = sum(grades)
    avg = total / len(grades)
    return avg

print(f"The grade average is {calc_avg(grades)}")


# Task 2: Implement a function to find the highest and lowest grade.

def find_high(grades):
    highest = max(grades)
    return highest

def find_low(grades):
    lowest = min(grades)
    return lowest

print(f"The highest grade is {find_high(grades)}")
print(f"The lowest grade is {find_low(grades)}")


# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def categorize_grade(grade):
    # letter_grades = []
    for grade in grades:
        if grade >= 90:
            grades[grade] = "A"
        elif grade >= 80:
            grades[grade] = "B"
        elif grade >= 70:
            grades[grade] = "C"
        elif grade >= 60:
            grades[grade] = "D"
        else:
            grades[grade] = "F"
    return grades

print(f"The letter grades are {categorize_grade(grades)}")

# Trying to debub IndexError