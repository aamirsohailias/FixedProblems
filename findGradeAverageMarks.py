def find_average(marks):
    subjects = len(marks)
    sum_of_maks = sum(marks)
    average = sum_of_maks / subjects
    return average
def find_grade(average):
    if average > 90:
        grade = 'A'
    elif average > 80:
        grade = 'B'
    elif average > 70:
        grade = 'C'
    else:
        grade =  'F'
    return grade
if __name__ == '__main__':
    marks = [100, 85, 90, 80, 65]
    average_of_marks = find_average(marks)
    print('average of marks is: ', average_of_marks)
    grade_of_subjects = find_grade(average_of_marks)
    print(grade_of_subjects)