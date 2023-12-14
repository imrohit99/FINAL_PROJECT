import sqlite3

connection = sqlite3.connect("student_scholarship_db.db")


def get_students_and_scholarships(student_id=None):
    cursor = connection.cursor()
    if student_id is None:
        rows = cursor.execute("SELECT students.*, scholarships.ScholarshipName FROM students LEFT JOIN scholarships ON students.ScholarshipID = scholarships.ScholarshipID")
    else:
        rows = cursor.execute(
            f"SELECT students.*, scholarships.ScholarshipName FROM students LEFT JOIN scholarships ON students.ScholarshipID = scholarships.ScholarshipID WHERE students.StudentID={student_id}")
    rows = list(rows)
    rows = [{'StudentID': row[0], 'FirstName': row[1], 'LastName': row[2], 'Gender': row[3],
             'DateOfBirth': row[4], 'Nationality': row[5], 'PassportNumber': row[6],
             'VisaStatus': row[7], 'Major': row[8], 'GPA': row[9], 'EnrollmentDate': row[10],
             'GraduationDate': row[11], 'ContactEmail': row[12], 'ContactPhone': row[13], 'ScholarshipName': row[14]} for row in rows]
    return rows


def add_student_and_scholarship(first_name, last_name, gender, date_of_birth, nationality, passport_number,
                                visa_status, major, gpa, enrollment_date, graduation_date, contact_email, contact_phone,
                                scholarship_name):
    cursor = connection.cursor()

    # Add scholarship
    cursor.execute("INSERT INTO scholarships (ScholarshipName) VALUES (?)", (scholarship_name,))
    connection.commit()

    # Get the last inserted ScholarshipID
    cursor.execute("SELECT last_insert_rowid()")
    scholarship_id = cursor.fetchone()[0]

    # Add student
    cursor.execute(
        "INSERT INTO students (FirstName, LastName, Gender, DateOfBirth, Nationality, PassportNumber, VisaStatus, Major, GPA, EnrollmentDate, GraduationDate, ContactEmail, ContactPhone, ScholarshipID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (first_name, last_name, gender, date_of_birth, nationality, passport_number, visa_status, major, gpa,
         enrollment_date, graduation_date, contact_email, contact_phone, scholarship_id))
    connection.commit()

def search_students_by_last_name(target_last_name):
    cursor = connection.cursor()
    target_last_name = target_last_name.lower()
    cursor.execute("SELECT * FROM students WHERE LOWER(LastName) = ?", (target_last_name,))
    matching_students = cursor.fetchall()
    return matching_students


def update_student_and_scholarship(student_id, first_name, last_name, gender, date_of_birth, nationality,
                                   passport_number, visa_status, major, gpa, enrollment_date, graduation_date,
                                   contact_email, contact_phone, scholarship_name):
    cursor = connection.cursor()

    # Update scholarship
    cursor.execute("UPDATE scholarships SET ScholarshipName=? WHERE ScholarshipID=(SELECT ScholarshipID FROM students WHERE StudentID=?)",
                   (scholarship_name, student_id))
    connection.commit()

    # Update student
    cursor.execute(
        "UPDATE students SET FirstName=?, LastName=?, Gender=?, DateOfBirth=?, Nationality=?, PassportNumber=?, VisaStatus=?, Major=?, GPA=?, EnrollmentDate=?, GraduationDate=?, ContactEmail=?, ContactPhone=? WHERE StudentID=?",
        (first_name, last_name, gender, date_of_birth, nationality, passport_number, visa_status, major, gpa,
         enrollment_date, graduation_date, contact_email, contact_phone, student_id))
    connection.commit()


def delete_student_and_scholarship(student_id):
    cursor = connection.cursor()

    # Delete student
    cursor.execute("DELETE FROM students WHERE StudentID=?", (student_id,))

    # Note: Deleting the student automatically removes the associated scholarship due to the foreign key constraint
    connection.commit()


def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("DROP TABLE IF EXISTS scholarships")
    except Exception as e:
        print(f"Error dropping tables: {e}")

    # Create the 'students' table
    cursor.execute(
        "CREATE TABLE students (StudentID INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Gender TEXT, DateOfBirth DATE, Nationality TEXT, PassportNumber TEXT, VisaStatus TEXT, Major TEXT, GPA DECIMAL(3, 2), EnrollmentDate DATE, GraduationDate DATE, ContactEmail TEXT, ContactPhone TEXT, ScholarshipID INTEGER, FOREIGN KEY (ScholarshipID) REFERENCES scholarships(ScholarshipID))")

    # Create the 'scholarships' table
    cursor.execute("CREATE TABLE scholarships (ScholarshipID INTEGER PRIMARY KEY, ScholarshipName TEXT)")

    # Insert sample data
    add_student_and_scholarship("Rohit", "Vedere", "Male", "1999-08-17", "INDIA", "ABC123456", "Student Visa", "Computer Science", 3.8, "2023-08-21", "2025-12-25", "svedere@kent.edu", "+1 234-282-1234", "Teaching Assistant")
    add_student_and_scholarship("ABC", "XYZ", "Female", "1996-11-22", "Spain", "XYZ789012", "Student Visa", "Engineering", 3.9, "2021-08-25", "2025-05-22", "xyz@kent.edu", "+1 234-567-8901", "Graudate Assistant")
    add_student_and_scholarship("Bruce", "wayne", "Male", "1997-03-10", "Gotham", "PQR345678", "Student Visa", "Business Administration", 3.5, "2023-01-10", "2025-05-10", "wayne@kent.edu", "+1 345-678-9012", "Athelete Scholarship")

    connection.commit()


if __name__ == "__main__":
    set_up_database()
    items = get_students_and_scholarships()
    print("Database Setup Completed.")
    print("Sample Data:")
    print(items)
    connection.close()
