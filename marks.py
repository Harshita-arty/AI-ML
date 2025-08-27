import matplotlib.pyplot as plt

marks1 = [85, 90, 78, 92, 88]
marks2= [10,20,30,40,50]
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

plt.bar(students, marks1, color='red')
plt.bar(students, marks2, align='edge', color='orange')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students - Day 3")
plt.show()