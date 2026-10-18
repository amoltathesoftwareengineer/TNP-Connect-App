
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)


class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    eligibility = db.Column(db.String(200), default="Open to eligible students")


@app.route("/")
def home():
    students = Student.query.order_by(Student.name).all()
    jobs = JobPosting.query.order_by(JobPosting.company).all()
    return render_template(
        "index.html",
        students=students,
        jobs=jobs
    )


@app.route("/students", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    department = request.form.get("department", "").strip()

    if not name or not email or not department:
        flash("Please complete all student fields.")
        return redirect(url_for("home"))

    if Student.query.filter_by(email=email).first():
        flash("This email is already registered.")
        return redirect(url_for("home"))

    db.session.add(Student(
        name=name,
        email=email,
        department=department
    ))
    db.session.commit()
    flash("Student added successfully.")
    return redirect(url_for("home"))


@app.route("/jobs", methods=["POST"])
def add_job():
    company = request.form.get("company", "").strip()
    title = request.form.get("title", "").strip()
    eligibility = request.form.get("eligibility", "").strip()

    if not company or not title:
        flash("Company and job title are required.")
        return redirect(url_for("home"))

    db.session.add(JobPosting(
        company=company,
        title=title,
        eligibility=eligibility or "Open to eligible students"
    ))
    db.session.commit()
    flash("Job posting added successfully.")
    return redirect(url_for("home"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
