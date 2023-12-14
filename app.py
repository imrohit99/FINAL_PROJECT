from bottle import route, post, run, template, redirect, request
import database

# Call set_up_database to create tables and insert sample data
database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    # Fetch data from both tables
    students_and_scholarships = database.get_students_and_scholarships()
    return template("list", data=students_and_scholarships)

@route("/add_student")
def get_add_student():
    return template("add_student.tpl")

@post("/add_student")
def post_add_student():
    # Add international student
    # Modify the function call based on your actual implementation
    database.add_international_student(
        request.forms.get("first_name"),
        request.forms.get("last_name"),
        request.forms.get("gender"),
        # Add other fields as needed
    )
    redirect("/list")

@route("/add_scholarship")
def get_add_scholarship():
    return template("add_scholarship.tpl")

@post("/add_scholarship")
def post_add_scholarship():
    # Add scholarship
    # Modify the function call based on your actual implementation
    database.add_scholarship(
        request.forms.get("scholarship_name"),
        request.forms.get("description"),
        # Add other fields as needed
    )
    redirect("/list")

@route("/delete/<student_id>")
def get_delete(student_id):
    student_info = database.get_students_and_scholarships(student_id)
    return template("delete", student=student_info[0])

@route("/delete/<student_id>", method="POST")
def post_delete(student_id):
    # Delete the student record
    database.delete_student_and_scholarship(student_id)
    redirect("/list")

@route("/add")
def get_add():
    # You might need to create a corresponding template for adding students and scholarships
    return template("add")

@post("/add_student")
def post_add_student():
    # Add international student
    # Modify the function call based on your actual implementation
    database.add_student_and_scholarship(
        request.forms.get("first_name"),
        request.forms.get("last_name"),
        request.forms.get("gender"),
        request.forms.get("date_of_birth"),
        request.forms.get("nationality"),
        request.forms.get("passport_number"),
        request.forms.get("visa_status"),
        request.forms.get("major"),
        request.forms.get("gpa"),
        request.forms.get("enrollment_date"),
        request.forms.get("graduation_date"),
        request.forms.get("contact_email"),
        request.forms.get("contact_phone"),
        request.forms.get("scholarship_name")
    )
    redirect("/list")


@route("/update/<student_id>")
def get_update(student_id):
    # Fetch the data of the student and scholarship with the given ID
    student_info = database.get_students_and_scholarships(student_id)
    
    # Render the update template with the fetched data
    return template("update", student=student_info[0])

@route("/update/<student_id>", method="POST")
def post_update(student_id):
    # Extract the updated data from the form
    # Update the function call based on your actual implementation
    database.update_student_and_scholarship(
        student_id,
        request.forms.get("first_name"),
        request.forms.get("last_name"),
        request.forms.get("gender"),
        request.forms.get("date_of_birth"),
        request.forms.get("nationality"),
        request.forms.get("passport_number"),
        request.forms.get("visa_status"),
        request.forms.get("major"),
        request.forms.get("gpa"),
        request.forms.get("enrollment_date"),
        request.forms.get("graduation_date"),
        request.forms.get("contact_email"),
        request.forms.get("contact_phone"),
        request.forms.get("scholarship_name")
    )
    redirect("/list")


@route("/search")
def get_search():
    return template("search")

@route("/search", method="POST")
def post_search():
    target_last_name = request.forms.get("last_name")
    matching_students = database.search_students_by_last_name(target_last_name)
    return template("search_data", data=matching_students)


run(host='localhost', port=8080)
