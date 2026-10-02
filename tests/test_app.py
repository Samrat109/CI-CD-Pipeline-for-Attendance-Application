from app import app


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
