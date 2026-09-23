"""
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

print(students[0])
print(students[1])
print(students[2])


for student in students:
    print(student)



for i in range(len(students)):
    print(i + 1, students[i])


students = {
    "Hermoine": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}
print(students["Hermoine"])
print(students["Draco"])
print()

for student in students:
    print(student, students[student], sep=", ")

"""
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
