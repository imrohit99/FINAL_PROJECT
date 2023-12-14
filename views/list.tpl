<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>International Students and Scholarships</title>
    <style>
         body {
            text-align: center;
        }

        h2 {
            color: blue;
        }

        table {
            margin: 0 auto; /* Center the table */
        }

        .header-links {
            text-align: right;
            margin-top: 10px;
            margin-bottom: 10px;
            margin-right:150px;
            font-size:30px;
        }

        a {
            display: inline-block;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="header-links">
        <a href="/search">Search</a>
    </div>
    <h2>International Students and Scholarships</h2>
    <table border="1">
        <tr>
            <th>Student ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Gender</th>
            <th>Date of Birth</th>
            <th>Nationality</th>
            <th>Passport Number</th>
            <th>Visa Status</th>
            <th>Major</th>
            <th>GPA</th>
            <th>Enrollment Date</th>
            <th>Graduation Date</th>
            <th>Contact Email</th>
            <th>Contact Phone</th>
            <th>Scholarship Name</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in data:
            <tr>
                <td>{{item['StudentID']}}</td>
                <td>{{item['FirstName']}}</td>
                <td>{{item['LastName']}}</td>
                <td>{{item['Gender']}}</td>
                <td>{{item['DateOfBirth']}}</td>
                <td>{{item['Nationality']}}</td>
                <td>{{item['PassportNumber']}}</td>
                <td>{{item['VisaStatus']}}</td>
                <td>{{item['Major']}}</td>
                <td>{{item['GPA']}}</td>
                <td>{{item['EnrollmentDate']}}</td>
                <td>{{item['GraduationDate']}}</td>
                <td>{{item['ContactEmail']}}</td>
                <td>{{item['ContactPhone']}}</td>
                <td>{{item['ScholarshipName']}}</td>
                <td><a href="/update/{{item['StudentID']}}">Update</a></td>
                <td><a href="/delete/{{item['StudentID']}}">Delete</a></td>
            </tr>
        % end
    </table><br><br>
    <a style="font-size:30px;" href="/add_student">Add a new student and scholarship</a>
</body>
</html>
