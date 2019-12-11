# Used this video for test setup: https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=8&t=0s
from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_all_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/all_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_categories(self):
        tester = app.test_client(self)
        response = tester.get('/categories', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
