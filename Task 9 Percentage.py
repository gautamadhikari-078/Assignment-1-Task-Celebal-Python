if __name__ == '__main__':
    n = int(input())  # Number of students' records
    
    student_marks = {}  # Dictionary to store name : marks pairs
    
    # Read each student's name and marks and store in dictionary
    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks
    
    query_name = input()  # Name of student to query
    
    # Get the marks for the student with query_name
    marks = student_marks[query_name]
    
    # Calculate the average marks
    average_marks = sum(marks) / len(marks)
    
    # Print the average marks formatted to 2 decimal places
    print(f"{average_marks:.2f}")
