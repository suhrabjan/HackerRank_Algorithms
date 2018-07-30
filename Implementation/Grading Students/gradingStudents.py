def gradingStudents(grades):
    result = []
    for num in grades:
        if num < 38:
            result.append(num)
        elif num % 5 > (5 - num % 5):
            result.append(num - num % 5 + 5)
        else:
            result.append(num)
    return result
