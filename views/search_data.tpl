<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Students</title>
</head>
<body>
    <h2>List of Students</h2>
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
                <td>{{item[0]}}</td>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
                <td>{{item[3]}}</td>
                <td>{{item[4]}}</td>
                <td>{{item[5]}}</td>
                <td>{{item[6]}}</td>
                <td>{{item[7]}}</td>
                <td>{{item[8]}}</td>
                <td>{{item[9]}}</td>
                <td>{{item[10]}}</td>
                <td>{{item[11]}}</td>
                <td>{{item[12]}}</td>
                <td>{{item[13]}}</td>
                <td>{{item[14]}}</td>
                <td><a href="/update/{{item[0]}}">Update</a></td>
                <td><a href="/delete/{{item[0]}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/list">Back to List</a>
</body>
</html>
