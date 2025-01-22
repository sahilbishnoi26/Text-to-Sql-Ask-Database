import sqlite3

# Database setup: Create a connection to the database
connection = sqlite3.connect("student.db")

# Create a cursor to interact with the database
cursor = connection.cursor()

# Create the `COURSE` table to store course details
create_course_table_query = """
CREATE TABLE IF NOT EXISTS COURSE (
    COURSE_ID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each course
    COURSE_NAME VARCHAR(50) NOT NULL,            -- Name of the course (required)
    CREDITS INTEGER NOT NULL                     -- Number of credits for the course
);
"""

# Create the `STUDENT` table with additional fields and primary key
create_student_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT (
    STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each student
    NAME VARCHAR(50) NOT NULL,                     -- Student's name (required)
    COURSE_ID INTEGER,                             -- Foreign key referencing the COURSE table
    SECTION VARCHAR(25),                           -- Section information
    MARKS INT,                                     -- Marks scored by the student
    FOREIGN KEY (COURSE_ID) REFERENCES COURSE (COURSE_ID) -- Relationship with COURSE table
);
"""

# Execute the table creation queries
cursor.execute(create_course_table_query)
cursor.execute(create_student_table_query)

# Insert realistic course records
course_values = [
    ('Data Science', 4),
    ('DevOps', 3),
    ('Machine Learning', 4),
    ('Cybersecurity', 3),
    ('Artificial Intelligence', 4)
]
cursor.executemany("INSERT INTO COURSE (COURSE_NAME, CREDITS) VALUES (?, ?)", course_values)

# Insert realistic student records
student_values = [
    ('Alice Johnson', 1, 'A', 92),  # Enrolled in Data Science
    ('Robert Smith', 1, 'B', 85),  # Enrolled in Data Science
    ('Evelyn Martinez', 2, 'A', 76),  # Enrolled in DevOps
    ('Michael Brown', 3, 'A', 88),  # Enrolled in Machine Learning
    ('Sophia Wilson', 4, 'B', 67),  # Enrolled in Cybersecurity
    ('David Lee', 5, 'A', 91),  # Enrolled in Artificial Intelligence
    ('Olivia Garcia', 1, 'B', 95),  # Enrolled in Data Science
    ('James Anderson', 3, 'A', 72)  # Enrolled in Machine Learning
]
cursor.executemany("INSERT INTO STUDENT (NAME, COURSE_ID, SECTION, MARKS) VALUES (?, ?, ?, ?)", student_values)

# Commit the changes
connection.commit()

# Display the `STUDENT` table records
print("Students:")
students = cursor.execute("""
SELECT S.STUDENT_ID, S.NAME, C.COURSE_NAME, S.SECTION, S.MARKS
FROM STUDENT S
JOIN COURSE C ON S.COURSE_ID = C.COURSE_ID
""")
for row in students:
    print(row)

# Display the `COURSE` table records
print("\nCourses:")
courses = cursor.execute("SELECT * FROM COURSE")
for row in courses:
    print(row)

# Close the connection
if connection:
    connection.close()
