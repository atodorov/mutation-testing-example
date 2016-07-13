import sandwich
import unittest

class TestBurger(unittest.TestCase):
    def test_default_burger_creation(self):
        burger = sandwich.Burger().make_sandwich()
        self.assertTrue(burger['type'] == 'burger')

    def test_default_burger_creation_and_check_default_values(self):
        burger = sandwich.Burger().make_sandwich()
        self.assertEqual(burger['type'], 'burger')
        self.assertEqual(burger['ham'], 1)

if __name__ == "__main__":
    unittest.main()
