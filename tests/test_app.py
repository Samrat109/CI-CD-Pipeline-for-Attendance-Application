from app import app, attendance, students


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Attendance Management System" in response.data


def test_register_page():
    client = app.test_client()
    response = client.get("/register")

    assert response.status_code == 200


def test_attendance_page():
    client = app.test_client()
    response = client.get("/attendance")

    assert response.status_code == 200


def test_home_attendance_form_posts_to_attendance_route():
    client = app.test_client()
    students.clear()
    students.append({"name": "Rahul", "roll_no": "101"})
    response = client.get("/")

    assert b'action="/attendance"' in response.data

    response = client.post(
        "/attendance",
        data={
            "student": "Rahul",
            "status": "Present"
        }
    )

    assert response.status_code == 302
    assert response.location == "/"


def test_attendance_without_registered_students_shows_registration_prompt():
    client = app.test_client()
    students.clear()
    attendance.clear()

    response = client.post("/attendance")

    assert response.status_code == 200
    assert b"Register a student before marking attendance." in response.data
    assert b"No students have been registered yet." in response.data
    assert attendance == []


def test_register_student():
    client = app.test_client()

    response = client.post(
        "/register",
        data={
            "name": "Rahul",
            "roll_no": "101"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Rahul" in response.data
