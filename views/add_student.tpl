<html>
<body>
<h2>Add New International Student and Scholarship</h2>
<hr/>

<form action="/add_student" method="post">
    <!-- Add input fields for first_name, last_name, gender, etc. -->
  <p>First Name: <input name="first_name" required/></p>
  <p>Last Name: <input name="last_name" required/></p>
  <p>Gender: <input name="gender" required/></p>
  <p>Date of Birth: <input name="date_of_birth" type="date" required/></p>
  <p>Nationality: <input name="nationality" required/></p>
  <p>Passport Number: <input name="passport_number" required/></p>
  <p>Visa Status: <input name="visa_status" required/></p>
  <p>Major: <input name="major" required/></p>
  <p>GPA: <input name="gpa" type="number" step="0.01" required/></p>
  <p>Enrollment Date: <input name="enrollment_date" type="date" required/></p>
  <p>Graduation Date: <input name="graduation_date" type="date" required/></p>
  <p>Contact Email: <input name="contact_email" type="email" required/></p>
  <p>Contact Phone: <input name="contact_phone" required/></p>
  <p>Scholarship Name: <input name="scholarship_name" required/></p>

    <button type="submit">Submit</button>
</form>

<hr/>
<a href="/">Back to List</a>
<hr/>
</body>
</html>
