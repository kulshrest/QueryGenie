import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(50), 
    CLASS VARCHAR(50), 
    SECTION VARCHAR(50), 
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert records into the STUDENT table
students = [
    ('Kamal', 'Data Science', 'A', 80),
    ('Suraj', 'Machine Learning', 'A', 90),
    ('Amit', 'Machine Learning', 'A', 85),
    ('Amrit', 'Data Science', 'B', 70),
    ('Kunal', 'Data Science', 'B', 50),
    ('Nisha', 'Industrial Internet of Things', 'A', 88),
    ('Ravi', 'Automation and Robotics', 'C', 67),
    ('Anita', 'Data Science', 'B', 75),
    ('Sahil', 'Machine Learning', 'C', 65),
    ('Priya', 'Industrial Internet of Things', 'B', 78),
    ('Vikas', 'Automation and Robotics', 'A', 92),
    ('Pooja', 'Data Science', 'C', 64),
    ('Manish', 'Machine Learning', 'B', 74),
    ('Sanjana', 'Industrial Internet of Things', 'C', 61),
    ('Rohit', 'Automation and Robotics', 'B', 81),
    ('Shreya', 'Data Science', 'D', 55),
    ('Aman', 'Machine Learning', 'B', 76),
    ('Bhavna', 'Industrial Internet of Things', 'D', 54),
    ('Raj', 'Automation and Robotics', 'A', 89),
    ('Geeta', 'Data Science', 'E', 49),
    ('Ajay', 'Machine Learning', 'C', 63),
    ('Anjali', 'Industrial Internet of Things', 'E', 45),
    ('Deepak', 'Automation and Robotics', 'B', 80),
    ('Meena', 'Data Science', 'F', 30),
    ('Sunil', 'Machine Learning', 'D', 58),
    ('Neha', 'Industrial Internet of Things', 'C', 60),
    ('Ashok', 'Automation and Robotics', 'A', 91),
    ('Lakshmi', 'Data Science', 'B', 77),
    ('Mohit', 'Machine Learning', 'F', 33),
    ('Poonam', 'Industrial Internet of Things', 'B', 82),
    ('Karan', 'Automation and Robotics', 'C', 62),
    ('Suman', 'Data Science', 'A', 85),
    ('Alok', 'Machine Learning', 'C', 68),
    ('Ritika', 'Industrial Internet of Things', 'A', 87),
    ('Vijay', 'Automation and Robotics', 'D', 59),
    ('Mona', 'Data Science', 'E', 40),
    ('Gaurav', 'Machine Learning', 'B', 79),
    ('Megha', 'Industrial Internet of Things', 'A', 90),
    ('Isha', 'Automation and Robotics', 'F', 28),
    ('Keshav', 'Data Science', 'C', 66),
    ('Rekha', 'Machine Learning', 'D', 53),
    ('Prakash', 'Industrial Internet of Things', 'C', 69),
    ('Sarita', 'Automation and Robotics', 'A', 88),
    ('Dev', 'Data Science', 'B', 83),
    ('Ishita', 'Machine Learning', 'B', 72),
    ('Anil', 'Industrial Internet of Things', 'D', 52),
    ('Vimal', 'Automation and Robotics', 'E', 44),
    ('Sneha', 'Data Science', 'A', 86),
    ('Ramesh', 'Machine Learning', 'C', 65),
    ('Swati', 'Industrial Internet of Things', 'B', 81),
    ('Preeti', 'Automation and Robotics', 'F', 32),
    ('Harish', 'Data Science', 'E', 48),
    ('Komal', 'Machine Learning', 'C', 70),
    ('Naveen', 'Industrial Internet of Things', 'D', 51),
    ('Divya', 'Automation and Robotics', 'A', 93),
    ('Tarun', 'Data Science', 'F', 31),
    ('Seema', 'Machine Learning', 'B', 73),
    ('Yogesh', 'Industrial Internet of Things', 'C', 64),
    ('Anshu', 'Automation and Robotics', 'D', 56),
    ('Gopal', 'Data Science', 'A', 84),
    ('Monika', 'Machine Learning', 'F', 29),
    ('Shyam', 'Industrial Internet of Things', 'B', 79),
    ('Reena', 'Automation and Robotics', 'E', 42),
    ('Nitin', 'Data Science', 'D', 57),
    ('Suresh', 'Machine Learning', 'C', 71),
    ('Pinky', 'Industrial Internet of Things', 'A', 89),
    ('Jatin', 'Automation and Robotics', 'B', 77),
    ('Payal', 'Data Science', 'E', 43),
    ('Chirag', 'Machine Learning', 'F', 30),
    ('Aarti', 'Industrial Internet of Things', 'B', 82),
    ('Varun', 'Automation and Robotics', 'D', 50),
    ('Ankur', 'Data Science', 'C', 63),
    ('Manoj', 'Machine Learning', 'B', 78),
    ('Jyoti', 'Industrial Internet of Things', 'A', 90),
    ('Ashish', 'Automation and Robotics', 'E', 41),
    ('Radha', 'Data Science', 'D', 54),
    ('Rohan', 'Machine Learning', 'C', 67),
    ('Vandana', 'Industrial Internet of Things', 'A', 88),
    ('Siddharth', 'Automation and Robotics', 'B', 80),
    ('Kirti', 'Data Science', 'F', 33),
    ('Rahul', 'Machine Learning', 'D', 58),
    ('Priti', 'Industrial Internet of Things', 'C', 66),
    ('Aakash', 'Automation and Robotics', 'A', 86),
    ('Lavanya', 'Data Science', 'B', 83),
    ('Sandeep', 'Machine Learning', 'E', 45),
    ('Neeraj', 'Industrial Internet of Things', 'D', 52),
    ('Kavita', 'Automation and Robotics', 'F', 29),
    ('Tushar', 'Data Science', 'A', 92),
    ('Ankita', 'Machine Learning', 'C', 68),
]


cursor.executemany('INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?,?,?,?)', students)

# Commit the changes and close the connection
connection.commit()
connection.close()
