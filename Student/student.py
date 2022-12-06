# Import the sqlite3 module
import sqlite3

# Connect to the database file
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query to retrieve the number of students
cursor.execute('SELECT COUNT(*) FROM students')
num_students = cursor.fetchone()[0]

# Execute a SQL query to retrieve the average grade of all students
cursor.execute('SELECT AVG(grade) FROM students')
avg_grade = cursor.fetchone()[0]

# Print the number of students and the average grade of all students
print('Number of students:', num_students)
print('Average grade:', avg_grade)

# Close the cursor and the connection to the database
cursor.close()
conn.close()