from collections import namedtuple

def main():
    # 1. Read the number of students
    n = int(input())
    
    # 2. Read the column names and create the namedtuple blueprint
    # .split() safely handles any uneven spaces or tabs between the headers
    columns = input().split()
    Student = namedtuple('Student', columns)
    
    total_marks = 0
    
    # 3. Loop through exactly 'n' rows
    for _ in range(n):
        row = input().split()
        
        # Unpack the row data into our Student blueprint
        student = Student(*row)
        
        # Add the marks to our total
        total_marks += int(student.MARKS)
        
    # 4. Calculate average and format to exactly 2 decimal places
    # Using .format() is bulletproof on all Python 3 versions
    print('{:.2f}'.format(total_marks / n))

if __name__ == '__main__':
    main()
