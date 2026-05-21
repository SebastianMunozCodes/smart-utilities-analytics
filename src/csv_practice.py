# 1. Create one student dictionary
student = {
    "name": "Sebastian", 
    "student_id": "sm3452", 
    "year": "senior", 
    "gpa": "3.7",
    "credits_completed": "102"
}

# Print student's name and gpa
print(f'Name: {student["name"]}')
print(f'GPA: {student["gpa"]}')
print(" ")

# 2. Create a list of student dictionaries
students = [
    {"name": "Sebastian", "student_id": "sm3452", "year": "senior", "gpa": "3.7", "credits_completed": "102"},
    {"name": "Alex", "student_id": "ah1345", "year": "junior", "gpa": "3.9", "credits_completed": "90"},
    {"name": "Maria", "student_id": "ms7465", "year": "sophomore", "gpa": "3.5", "credits_completed": "52"},
    {"name": "Jordan", "student_id": "jj4533", "year": "junior", "gpa": "3.2", "credits_completed": "50"},
    {"name": "Taylor", "student_id": "th4593", "year": "freshman", "gpa": "3.8", "credits_completed": "36"},
    {"name": "Ben", "student_id": "bl8639", "year": "senior", "gpa": "3.9", "credits_completed": "105"}
]

# 3. Print all Students
for i in students:
    print(f'{i["name"]} - {i["year"]} - {float(i["gpa"])}')
print(" ")

# 4. Calculate the average GPA
total = 0
count = 0
for i in students:
    total += float(i["gpa"])
    count += 1
avg = total / count
print(f'Average GPA: {avg:.2f}')
print(" ")

# 5. Find the student with the highest GPA
best_gpa = max(students, key=lambda student: float(student["gpa"]))
max_gpa = float(best_gpa["gpa"])
highest_gpas = [student for student in students if float(student["gpa"]) == max_gpa]
print("Student(s) with the highest gpa:")
for student in highest_gpas:
    print(f'{student["name"]}: {student["gpa"]}')
print(" ")

# 6. Count how many students are juniors
junior_count = 0
for student in students:
    if student["year"] == "junior":
        junior_count +=1
print(f'Amount of juniors: {junior_count}')

# 7. Count how many students have at least 60 credits
credit_count = 0
for student in students:
    total_credits = int(student["credits_completed"])
    if total_credits >= 60:
        credit_count +=1
print(f'Amount of students with at least 60 credits completed: {credit_count}')