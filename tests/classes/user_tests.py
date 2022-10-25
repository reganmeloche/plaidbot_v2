import unittest
from src.classes.user import User

class UserTests(unittest.TestCase):
    def test_user(self):
        user = User('id1', 'test_name', 'real name')
        result = user.to_string()
        expected_result = 'id: id1, name: test_name, real_name: real name'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()