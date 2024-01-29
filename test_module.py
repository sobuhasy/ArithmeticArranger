import unittest
from arithmetic_arranger import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):
    def test_arithmetic_arranger(self):
        self.assertEqual(arithmetic_arranger(["52 + 54"]), "  52\n+ 54\n----")
    
    if __name__ == "__main__":
        unittest.main()