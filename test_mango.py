import unittest

from hello import add

class TestSum(unittest.TestCase):
    def test_add(self):
        assert add(49,51) == 100
    def test_add2(self):
        assert add(49,50) == 99


if __name__ == '__main__':
    unittest.main()
