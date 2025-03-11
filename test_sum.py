import unittest
from sum import add

class TestSum(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_addition_negative(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_addition_zero(self):
        self.assertEqual(add(0, 0), 0)
    
    def test_addition_large_numbers(self):
        self.assertEqual(add(1000000, 1000000), 2000000)

if __name__ == '__main__':
    # Generate JUnit-compatible XML report
    import xmlrunner
    with open('test-reports/test_results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), exit=False)
