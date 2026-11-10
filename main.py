# Student Performance Analysis

students = {
    "Ananya": [85, 90, 78],
    "Rahul": [70, 75, 80],
    "Priya": [95, 92, 98],
    "Arjun": [60, 65, 58],
    "Sneha": [88, 84, 91]
}

print("STUDENT PERFORMANCE ANALYSIS")
print("--------------------------------")

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)

    print("Student:", name)
    print("Total Marks:", total)
    print("Average:", round(average, 2))

    if average >= 85:
        print("Performance: Excellent")
    elif average >= 60:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

    print("--------------------------------")
