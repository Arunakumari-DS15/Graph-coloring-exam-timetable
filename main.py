
# Graph Coloring and Exam Timetable Scheduling

# Subjects offered by the college
subjects = ["ADSAA", "DBMS", "CN", "Python", "Mathematics"]

# Subjects registered by each student
students = {
    "S1": ["ADSAA", "DBMS"],
    "S2": ["ADSAA", "CN"],
    "S3": ["DBMS", "CN"],
    "S4": ["DBMS", "Python"],
    "S5": ["CN", "Mathematics"],
    "S6": ["Python", "Mathematics"]
}

# Create an empty graph
graph = {subject: set() for subject in subjects}

# Connect subjects that share students
for enrolled in students.values():
    for i in range(len(enrolled)):
        for j in range(i + 1, len(enrolled)):
            s1 = enrolled[i]
            s2 = enrolled[j]
            graph[s1].add(s2)
            graph[s2].add(s1)

# Available examination slots
slots = [
    "Day 1 - Morning",
    "Day 1 - Afternoon",
    "Day 2 - Morning"
]

# Store the assigned slot for each subject
assigned = {}

# Check whether a slot is safe for a subject
def can_assign(subject, slot):
    for neighbor in graph[subject]:
        if assigned.get(neighbor) == slot:
            return False
    return True

# Backtracking algorithm
def color_subject(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for slot in slots:
        if can_assign(subject, slot):
            assigned[subject] = slot

            if color_subject(index + 1):
                return True

            # Undo the assignment and try another slot
            del assigned[subject]

    return False

# Generate and display the timetable
if color_subject(0):
    print("EXAMINATION TIMETABLE")
    print("---------------------")
    for subject in subjects:
        print(subject, ":", assigned[subject])
else:
    print("No valid timetable is possible with these slots.")
