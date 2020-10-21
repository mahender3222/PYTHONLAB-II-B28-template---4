
""" write a program for Linear Search"""

# It returns index of x in given array arr if present, 
# else returns -1

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def linear_search(lst,key):
    pass
     
class TestLinearSearch(unittest.TestCase): 

    def test_01(self):
        lst = [1,2,3,4]
        key = 1
        self.assertEqual(linear_search(lst,key),0)

    def test_02(self):
        lst = [1,2,3,4]
        key = 5
        self.assertEqual(linear_search(lst,key),-1)

    def test_03(self):
        lst = [1,2,3,4]
        key = -1
        self.assertEqual(linear_search(lst,key),-1)

    def test_04(self):
        lst = [1,2,3,4]
        key = 4
        self.assertEqual(linear_search(lst,key),3)
 
if __name__ == '__main__':
    unittest.main(verbosity=2)

