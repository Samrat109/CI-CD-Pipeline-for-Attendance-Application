from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []
attendance = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        students=students,
        attendance=attendance
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        roll_no = request.form["roll_no"]

        students.append({
            "name": name,
            "roll_no": roll_no
        })

        return redirect("/")

    return render_template("register.html")


@app.route("/attendance", methods=["GET", "POST"])
def mark_attendance():

    if request.method == "POST":

        student = request.form["student"]
        status = request.form["status"]

        attendance.append({
            "student": student,
            "status": status
        })

        return redirect("/")

    return render_template(
        "attendance.html",
        students=students
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
