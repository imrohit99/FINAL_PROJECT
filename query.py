import sqlite3

connection = sqlite3.connect("student_scholarship_db.db")

cursor = connection.cursor()

# Fetch data from the 'InternationalStudents' table
cursor.execute("SELECT StudentID, FirstName, LastName, Gender, DateOfBirth, Nationality, PassportNumber, VisaStatus, Major, GPA, EnrollmentDate, GraduationDate, ContactEmail, ContactPhone FROM InternationalStudents")
student_rows = list(cursor.fetchall())

# Fetch data from the 'Scholarships' table
cursor.execute("SELECT ScholarshipID, ScholarshipName, RecipientID FROM Scholarships")
scholarship_rows = list(cursor.fetchall())

print("International Students:")
print(student_rows)

print("\nScholarships:")
print(scholarship_rows)

# Combine the data into a single list of dictionaries
student_data = [
    {
        'StudentID': row[0],
        'FirstName': row[1],
        'LastName': row[2],
        'Gender': row[3],
        'DateOfBirth': row[4],
        'Nationality': row[5],
        'PassportNumber': row[6],
        'VisaStatus': row[7],
        'Major': row[8],
        'GPA': row[9],
        'EnrollmentDate': row[10],
        'GraduationDate': row[11],
        'ContactEmail': row[12],
        'ContactPhone': row[13],
    } for row in student_rows
]

scholarship_data = [{'ScholarshipID': row[0], 'ScholarshipName': row[1], 'RecipientID': row[2]} for row in scholarship_rows]

print("\nCombined Data:")
combined_data = []

for student in student_data:
    related_scholarships = [scholarship for scholarship in scholarship_data if scholarship['RecipientID'] == student['StudentID']]
    student_copy = student.copy()
    student_copy['Scholarships'] = related_scholarships
    combined_data.append(student_copy)

print(combined_data)
