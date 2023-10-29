sub1_midterm = int(input("programming midterm: "))
sub1_final = int(input("programming final: "))
sub2_midterm = int(input("network midterm: "))
sub2_final = int(input("network final: "))
sub3_midterm = int(input("math midterm: "))
sub3_final = int(input("math final: "))
sub4_midterm = int(input("electronic midterm: "))
sub4_final = int(input("electronic final: "))
sub5_midterm = int(input("web design midterm: "))
sub5_final = int(input("web design final: "))

total = sub1_midterm + sub1_final + sub2_midterm + sub2_final + sub3_midterm + sub3_final + sub4_midterm + sub4_final + sub5_midterm + sub5_final
average = total / 10

# Harf notunu hesapla
if average >= 97:
    letter_grade = "A+"
    grade_point = 4.0
elif 94 <= average < 97:
    letter_grade = "A"
    grade_point = 4.0
elif 90 <= average < 94:
    letter_grade = "A-"
    grade_point = 3.7
elif 87 <= average < 90:
    letter_grade = "B+"
    grade_point = 3.3
elif 84 <= average < 87:
    letter_grade = "B"
    grade_point = 3.0
elif 80 <= average < 84:
    letter_grade = "B-"
    grade_point = 2.7
elif 77 <= average < 80:
    letter_grade = "C+"
    grade_point = 2.3
elif 74 <= average < 77:
    letter_grade = "C"
    grade_point = 2.0
elif 70 <= average < 74:
    letter_grade = "C-"
    grade_point = 1.7
elif 67 <= average < 70:
    letter_grade = "D+"
    grade_point = 1.3
elif 64 <= average < 67:
    letter_grade = "D"
    grade_point = 1.0
elif 60 <= average < 64:
    letter_grade = "D-"
    grade_point = 0.7
else:
    letter_grade = "F"
    grade_point = 0.0

print("----------------")
print("Letter Grade:", letter_grade)
print("Grade Point:", grade_point)