import unittest
from src.shared.printer import ConsolePrinter

class UserTests(unittest.TestCase):
    def setUp(self):
        self.sut = ConsolePrinter()
        
    def test_printer(self):
        self.sut.mprint('test')

if __name__ == '__main__':
    unittest.main()