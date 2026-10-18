
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)


class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    eligibility = db.Column(
        db.String(200),
        default="Open to eligible students",
    )


# Home Page
@app.route("/")
def home():
    students = Student.query.order_by(Student.name).all()
    jobs = JobPosting.query.order_by(JobPosting.company).all()

    return render_template(
        "index.html",
        students=students,
        jobs=jobs,
    )


# Register Student
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

    try:
        student = Student(
            name=name,
            email=email,
            department=department,
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully.")

    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Unable to register student.")
        flash("Unable to register student. Please try again.")

    return redirect(url_for("home"))


# Add Job Posting
@app.route("/jobs", methods=["POST"])
def add_job():
    company = request.form.get("company", "").strip()
    title = request.form.get("title", "").strip()
    eligibility = request.form.get("eligibility", "").strip()

    if not company or not title:
        flash("Company and job title are required.")
        return redirect(url_for("home"))

    try:
        job = JobPosting(
            company=company,
            title=title,
            eligibility=(
                eligibility or "Open to eligible students"
            ),
        )
        db.session.add(job)
        db.session.commit()
        flash("Job posting added successfully.")

    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Unable to create job posting.")
        flash("Unable to publish job. Please try again.")

    return redirect(url_for("home"))


# Custom Error Pages
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template("500.html"), 500


# Create Database Tables
with app.app_context():
    db.create_all()


# Run Application
if __name__ == "__main__":
    app.run(debug=True)
