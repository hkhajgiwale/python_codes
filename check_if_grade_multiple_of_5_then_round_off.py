# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the grade and the next multiple of 5  is less than 3 , round grade up to the next multiple of 5.
# If the value of  grade is less than 38, no rounding occurs as the result will still be a failing grade.

# Examples

#  1. grade = 84: round to  (85 - 84 is less than 3)
#  2. grade = 29: do not round (result is less than 40)
#  3. grade = 57: do not round (60 - 57 is 3 or higher)

result = []
grades = [73, 67, 38, 33]
grade=0
print(grades)
for i in grades:
    multiplier = int((i/5)+1)*5
    print(multiplier)
    if (i < 38):
        #print("IF LOOP")
        grade = i
    elif((multiplier - i) < 3):
        print(multiplier-i)
        grade = multiplier
    elif ((multiplier - i) >= 3):
        #print("ELSE")
        #print(multiplier-i)
        grade = i
    result.append(grade)
print(result)