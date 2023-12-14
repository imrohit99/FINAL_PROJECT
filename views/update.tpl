<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Student and Scholarship</title>
</head>
<body>
    <h2>Update Student and Scholarship</h2>
    <form action="/update/{{student['StudentID']}}" method="post">
        <p>First Name: <input name="first_name" value="{{student['FirstName']}}" required/></p>
        <p>Last Name: <input name="last_name" value="{{student['LastName']}}" required/></p>
        <p>Gender: <input name="gender" value="{{student['Gender']}}" required/></p>
        <p>Date of Birth: <input name="date_of_birth" type="date" value="{{student['DateOfBirth']}}" required/></p>
        <p>Nationality: <input name="nationality" value="{{student['Nationality']}}" required/></p>
        <p>Passport Number: <input name="passport_number" value="{{student['PassportNumber']}}" required/></p>
        <p>Visa Status: <input name="visa_status" value="{{student['VisaStatus']}}" required/></p>
        <p>Major: <input name="major" value="{{student['Major']}}" required/></p>
        <p>GPA: <input name="gpa" type="number" step="0.01" value="{{student['GPA']}}" required/></p>
        <p>Enrollment Date: <input name="enrollment_date" type="date" value="{{student['EnrollmentDate']}}" required/></p>
        <p>Graduation Date: <input name="graduation_date" type="date" value="{{student['GraduationDate']}}" required/></p>
        <p>Contact Email: <input name="contact_email" type="email" value="{{student['ContactEmail']}}" required/></p>
        <p>Contact Phone: <input name="contact_phone" value="{{student['ContactPhone']}}" required/></p>
        <p>Scholarship Name: <input name="scholarship_name" value="{{student['ScholarshipName']}}" required/></p>
        <p><button type="submit">Update</button></p>
    </form>
</body>
</html>
