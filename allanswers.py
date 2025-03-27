
1. Character Classification
def classify_character(char):
    if len(char) != 1:
        print("Invalid input")
    elif char.isdigit():
        print("Digit")
    elif char.islower():
        print("Lowercase Character")
    elif char.isupper():
        print("Uppercase Character")
    else:
        print("Special Character")

char = input("Enter a single character: ")
classify_character(char)

2. Fibonacci Sequence Until Sum Exceeds X
def fibonacci_until_x(x):
    if x < 0:
        print("Invalid input")
        return

    fib_seq = [0, 1]
    while sum(fib_seq) <= x:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    print(fib_seq[:-1])

x = int(input("Enter X: "))
fibonacci_until_x(x)

3. Armstrong Number Check
def is_armstrong(n):
    if n < 0:
        print("Invalid input")
        return
    digits = [int(d) for d in str(n)]
    if sum(d ** len(digits) for d in digits) == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

n = int(input("Enter a number: "))
is_armstrong(n)

4. Strong Numbers in a Range
import math

def is_strong(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

L, R = map(int, input("Enter L R: ").split())
strong_numbers = [n for n in range(L, R+1) if is_strong(n)]
print(strong_numbers if strong_numbers else "No Strong numbers found")

5. Matrix Addition
m, n = map(int, input("Enter m n: ").split())
matrix1 = [list(map(int, input().split())) for _ in range(m)]
matrix2 = [list(map(int, input().split())) for _ in range(m)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(m)]
for row in result:
    print(*row)

6. Sum of Primary Diagonal in a Square Matrix
N = int(input("Enter N: "))
matrix = [list(map(int, input().split())) for _ in range(N)]
print(sum(matrix[i][i] for i in range(N)))

7. Online Banking Password Validation
import re

password = input("Enter password: ")
if (6 <= len(password) <= 16 and 
    re.search(r'[a-z]', password) and
    re.search(r'[A-Z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[$#@]', password)):
    print("Password is valid")
else:
    print("Password is invalid")

8. Library Book Title Transformation
s1 = input("Enter title: ")
print(s1[:2] + s1[-2:] if len(s1) >= 2 else "-1")
print(s1[0] + s1[1:].replace(s1[0], "$") if s1 else "Invalid input")

str1, str2 = input().split()
print(str2[:2] + str1[2:] + " " + str1[:2] + str2[2:])

9. University Course Enrollment System
n = int(input("Enter number of students: "))
students = [input().split()[0] for _ in range(n)]
m = int(input("Enter number of courses: "))
courses = [input() for _ in range(m)]

print(sum(1 for s in students if s.startswith('a')))
print(len(students))
print("Data Science" in courses)
print(students + courses)

10. List of Temperatures in a Week
temps = list(map(int, input("Enter temperatures: ").split()))
transformed = [t * 5 for t in temps]
print(transformed)
print("Sorted:", sorted(set(transformed)))
print("Second smallest:", sorted(set(transformed))[1])

11. College Exam Marks Evaluation
n = int(input("Enter number of students: "))
for _ in range(n):
    reg, name, *marks = input().split()
    marks = list(map(int, marks))
    print(f"Total Marks: {sum(marks)}, Grade: {'A' if sum(marks) >= 250 else 'B' if sum(marks) >= 200 else 'C'}")

12. Calculate Areas of Geometric Shapes
import math

b, h, r, l, w = map(int, input().split())
print(f"{0.5 * b * h:.2f}")
print(f"{math.pi * r ** 2:.2f}")
print(f"{l * w:.2f}")

13. Budget Tracking (FOP Lab)
import csv

n = int(input("Enter number of categories: "))
with open("expenses.csv", "w") as file:
    writer = csv.writer(file)
    for _ in range(n):
        writer.writerow(input().split())

with open("expenses.csv", "r") as file:
    for row in csv.reader(file):
        print(row)

14. Ancient Scroll Security System
import math

def is_strong(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

L, R = map(int, input("Enter L R: ").split())
strong_numbers = [n for n in range(L, R+1) if is_strong(n)]
print(strong_numbers if strong_numbers else "No Strong numbers found")

15. Library Membership and Books Collection
n = int(input("Enter number of members: "))
members = [input().split()[0] for _ in range(n)]

m = int(input("Enter number of books: "))
books = [input() for _ in range(m)]

print(sum(1 for name in members if name.startswith('a')))
print(len(members))
print("Python Programming" in books)
print(members + books)

16. College Exam Marks Validation (With Exception Handling)
class InvalidMark(Exception): pass
class InvalidReg(Exception): pass

try:
    reg, name, *marks = input().split()
    if not reg.isdigit():
        raise InvalidReg("Invalid Register Number")
    marks = list(map(int, marks))
    if any(m > 100 for m in marks):
        raise InvalidMark("Invalid Marks")
    print("Valid Input")
except Exception as e:
    print(e)

17. Name and String Swapping
def name_swap(s1, s2):
    if len(s1) < 2 or len(s2) < 2:
        print("Invalid input")
        return
    print(s2[:2] + s1[2:] + " " + s1[:2] + s2[2:])

str1, str2 = input("Enter two names: ").split()
name_swap(str1, str2)

20. College Exam Report with Grading
n = int(input("Enter number of students: "))

for _ in range(n):
    reg_no, name, *marks = input().split()
    marks = list(map(int, marks))
    total = sum(marks)
    grade = "A" if total >= 250 else "B" if total >= 200 else "C"
    
    print(f"Register Number: {reg_no}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Grade: {grade}
")

