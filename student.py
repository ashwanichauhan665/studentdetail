# Function to calculate total score
def calculate_total(student):
    # Total is the sum of Hindi, English, Maths, Science, and Computer scores
    total = student[4] + student[5] + student[6] + student[7] + student[8]
    return total

# List to store student data
students = []

# Adding student data
students.append([1, 'Ashish'  , '10th',15,85,88,92,90,95, 0])  
students.append([2, 'Abhi'    , '10th',16,78,82,88,84,80, 0])   
students.append([3, 'Aman'    , '10th',15,90,92,94,93,96, 0])  
students.append([4, 'Kratika' , '10th',15,97,90,90,91,90, 0]) 
students.append([5, 'Mona'    , '10th',15,76,81,39,87,90, 0])  
students.append([6, 'Pratush' , '10th',16,64,72,58,94,70, 0])   
students.append([7, 'Ragini'  , '10th',15,92,95,91,92,59, 0])  
students.append([8, 'Kartik'  , '10th',15,78,69,70,88,76, 0]) 
students.append([9, 'Anshika' , '10th',15,88,81,50,70,51, 0])  
students.append([10,'Aira'    , '10th',16,63, 2,89,87,89, 0])  


# Calculate total score for each student
for student in students:
    student[9] = calculate_total(student)

# Print student data

cnt:int=0;

print("ID  | Name    | Standard | Age | Hindi | English | Maths | Science | Computer | Total  ")
print("----|---------|----------|-----|-------|---------|-------|---------|----------|--------")
for student in students:
    cnt = cnt + 1
    if cnt < 10:
        print(f"  {student[0]} | {student[1]:<7} | {student[2]:<8} | {student[3]:<3} | {student[4]:<5} | {student[5]:<7} | {student[6]:<5} | {student[7]:<7} | {student[8]:<8} | {student[9]:<5}")
    else:
        print(f" {student[0]} | {student[1]:<7} | {student[2]:<8} | {student[3]:<3} | {student[4]:<5} | {student[5]:<7} | {student[6]:<5} | {student[7]:<7} | {student[8]:<8} | {student[9]:<5}")
# Display names of students whose marks in English are greater than 50
print("\nNames of students whose marks in English are greater than 50:")
for student in students:
    if student[5] > 50:
        print(student[1])
        # Sort students by Maths score in descending order without using libraries
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][6] < students[j][6]:
            students[i], students[j] = students[j], students[i]

# Display name and age of top four scorers in Maths
print("\nName and age of top four scorers in Maths:")
for student in students[:4]:
    print(f"Name: {student[1]}, Age: {student[3]}")
    # Find bottom three scorers in Computer
bottom_three = sorted(students, key=lambda x: x[8])[:3]

# Display name, ID, and age of bottom three scorers in Computer
print("\nName, ID, and age of bottom three scorers in Computer:")
for student in bottom_three:
    print(f"Name: {student[1]}, ID: {student[0]}, Age: {student[3]}")