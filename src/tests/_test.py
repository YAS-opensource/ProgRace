from src import app

import unittest


class AppTestCase(unittest.TestCase):
    def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue("30%" in response.data.decode())

    def test_title_text(self):
        tester = app.test_client(self)

        response = tester.get("/?title=custom")
        self.assertTrue("custom" in response.data.decode())
        self.assertTrue("30%" in response.data.decode())

    def test_progress_text(self):
        tester = app.test_client(self)

        response = tester.get("/?progress=20")
        self.assertTrue("20%" in response.data.decode())
        self.assertTrue("#f07178" in response.data.decode())

        response = tester.get("/?progress=50")
        self.assertTrue("50%" in response.data.decode())
        self.assertTrue("#ffcb6b" in response.data.decode())

        response = tester.get("/?progress=90")
        self.assertTrue("90%" in response.data.decode())
        self.assertTrue("#c3e88d" in response.data.decode())

        response = tester.get("/?progress=110")
        self.assertTrue("100%" in response.data.decode())
        self.assertTrue("#c3e88d" in response.data.decode())

        response = tester.get("/?progress=1000")
        self.assertTrue("100%" in response.data.decode())
        self.assertTrue("#c3e88d" in response.data.decode())

    def test_total_progress_text(self):
        tester = app.test_client(self)

        response = tester.get("/?progress=100&total=200")
        self.assertTrue("50%" in response.data.decode())

        response = tester.get("/?progress=100&total=0")
        self.assertTrue("100%" in response.data.decode())

        response = tester.get("/?progress=755&total=1000")
        self.assertTrue("75%" in response.data.decode())


if __name__ == "__main__":
    unittest.main()
