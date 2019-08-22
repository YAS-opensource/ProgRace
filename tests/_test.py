from api.app import app

import unittest


class AppTestCase(unittest.TestCase):
    def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue("30%" in response.data.decode())


if __name__ == "__main__":
    unittest.main()
