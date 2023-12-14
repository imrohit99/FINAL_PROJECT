import sqlite3

connection = sqlite3.connect("student_scholarship_db.db")

cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS InternationalStudents")
    cursor.execute("DROP TABLE IF EXISTS Scholarships")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'InternationalStudents' table
try:
    cursor.execute("CREATE TABLE InternationalStudents (StudentID INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Gender TEXT, DateOfBirth DATE, Nationality TEXT, PassportNumber TEXT, VisaStatus TEXT, Major TEXT, GPA DECIMAL(3, 2), EnrollmentDate DATE, GraduationDate DATE, ContactEmail TEXT, ContactPhone TEXT)")
except Exception as e:
    print(f"Error creating 'InternationalStudents' table: {e}")

# Create the 'Scholarships' table
try:
    cursor.execute("CREATE TABLE Scholarships (ScholarshipID INTEGER PRIMARY KEY, ScholarshipName TEXT, RecipientID INTEGER, FOREIGN KEY (RecipientID) REFERENCES InternationalStudents(StudentID))")
except Exception as e:
    print(f"Error creating 'Scholarships' table: {e}")

# Insert sample data into 'InternationalStudents' table
students_data = [("Rohit", "Vedere", "Male", "1999-08-17", "INDIA", "ABC123456", "Student Visa", "Computer Science", 3.8, "2023-08-21", "2025-12-25", "svedere@kent.edu", "+1 234-282-1234"),
                 ("ABC", "XYZ", "Female", "1996-11-22", "Spain", "XYZ789012", "Student Visa", "Engineering", 3.9, "2021-08-25", "2025-05-22", "xyz@kent.edu", "+1 234-567-8901"),
                 ("Bruce", "wayne", "Male", "1997-03-10", "Gotham", "PQR345678", "Student Visa", "Business Administration", 3.5, "2023-01-10", "2025-05-10", "wayne@kent.edu", "+1 345-678-9012")]

for student_data in students_data:
    try:
        cursor.execute("INSERT INTO InternationalStudents (FirstName, LastName, Gender, DateOfBirth, Nationality, PassportNumber, VisaStatus, Major, GPA, EnrollmentDate, GraduationDate, ContactEmail, ContactPhone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", student_data)
    except Exception as e:
        print(f"Error inserting data into 'InternationalStudents' table: {e}")

# Insert sample data into 'Scholarships' table
scholarships_data = [('Merit Scholarship', 1),
                     ('Diversity Scholarship', 2),
                     ('STEM Excellence Scholarship', 3)]

for scholarship_data in scholarships_data:
    try:
        cursor.execute("INSERT INTO Scholarships (ScholarshipName, RecipientID) VALUES (?, ?)", scholarship_data)
    except Exception as e:
        print(f"Error inserting data into 'Scholarships' table: {e}")

connection.commit()
connection.close()
print("done.")
