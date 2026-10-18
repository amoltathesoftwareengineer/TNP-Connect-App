
import unittest

from app import app


class TNPConnectAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TNP Connect", response.data)

    def test_unknown_page_returns_404(self):
        response = self.client.get("/this-page-does-not-exist")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
