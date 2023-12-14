<!DOCTYPE html>
<html>
<head>
    <title>Delete Student Record</title>
</head>
<body>
    <h2>Delete Student Record</h2>
    <p>Are you sure you want to delete the following student record?</p>
    <p>
        <strong>Student ID:</strong> {{student['StudentID']}}<br>
        <strong>Name:</strong> {{student['FirstName']}} {{student['LastName']}}<br>
        <strong>Major:</strong> {{student['Major']}}<br>
        <strong>Scholarship Name:</strong> {{student['ScholarshipName']}}
    </p>
    <form action="/delete/{{student['StudentID']}}" method="post">
        <button type="submit">Confirm Delete</button>
    </form>
    <a href="/list">Cancel</a>
</body>
</html>
