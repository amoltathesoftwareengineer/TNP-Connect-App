
import unittest

from app import app


class TNPConnectAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_students_page_route(self):
        response = self.client.get("/students")
        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
    unittest.main()
