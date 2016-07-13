import sandwich
import unittest

class TestBurger(unittest.TestCase):
    def test_default_burger_creation(self):
        burger = sandwich.Burger().make_sandwich()
        self.assertTrue(burger['type'] == 'burger')

if __name__ == "__main__":
    unittest.main()
