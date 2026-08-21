# Read the number of students (N) and number of subjects (X)
n, x = map(int, input().split())

# Create a list to hold the marks for each subject
subject_marks = []

# Read the marks for each subject
for _ in range(x):
    # Convert input string to a map of floats and append to our list
    subject_marks.append(map(float, input().split()))

# zip(*subject_marks) unpacks the subjects and pairs the elements by index.
# This essentially groups all the 1st marks together (Student 1), 
# all 2nd marks together (Student 2), and so on.
for student_marks in zip(*subject_marks):
    # Calculate and print the average for each student
    print(sum(student_marks) / x)
