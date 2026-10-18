
import unittest

from app import app, db, Student, JobPosting


class TNPConnectAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
        self.app_context = app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TNP Connect", response.data)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "healthy"})

    def test_unknown_page_returns_404(self):
        response = self.client.get("/this-page-does-not-exist")
        self.assertEqual(response.status_code, 404)

    def test_student_registration(self):
        response = self.client.post("/students", data={
            "name": "Test Student",
            "email": "student@example.com",
            "department": "Computer Science",
        })
        self.assertEqual(response.status_code, 302)
        student = Student.query.filter_by(
            email="student@example.com"
        ).first()
        self.assertIsNotNone(student)

    def test_duplicate_student_email(self):
        student = Student(
            name="First Student",
            email="duplicate@example.com",
            department="IT",
        )
        db.session.add(student)
        db.session.commit()

        self.client.post("/students", data={
            "name": "Second Student",
            "email": "duplicate@example.com",
            "department": "Computer Science",
        })

        students = Student.query.filter_by(
            email="duplicate@example.com"
        ).all()
        self.assertEqual(len(students), 1)

    def test_job_posting(self):
        response = self.client.post("/jobs", data={
            "company": "Example Company",
            "title": "Junior SQL Developer",
            "eligibility": "Eligible students",
        })
        self.assertEqual(response.status_code, 302)
        job = JobPosting.query.filter_by(
            title="Junior SQL Developer"
        ).first()
        self.assertIsNotNone(job)


if __name__ == "__main__":
    unittest.main()
