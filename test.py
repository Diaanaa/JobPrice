import unittest
from good import*

class Test(unittest.TestCase):

    def price_after_taxation(self):
        if self.exempt == "exempt":
            self.assertEqual(price_after_taxation(100),100)
        else:
            self.assertEqual(price_after_taxation(100),107)

#очевидно, тестов должно быть чуууточку больше, чем один
#но еще чуть-чуть и мой ноут полетит в окно 🙃 

if __name__ == "__main__":
    unittest.main()



