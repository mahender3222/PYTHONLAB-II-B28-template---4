
""" write a program for Binary Search""" 
# It returns index of x in given array arr if present, 
# else returns -1

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def binary_search(lst,key):
     lst.sort()
    low = 0
    high = len(lst)-1
    while low<=high:
        middle=(low+high)//2
        if lst[middle] == key:
            return(middle)
        elif key<lst[middle]:
            high = middle-1
        else:
            low = middle+1
    return(-1)
     
# DO NOT TOUCH THE BELOW CODE
class TestBinarySearch(unittest.TestCase):
    
    def test_01(self):
        lst = [1,2,3,4]
        key = 5
        self.assertEqual(binary_search(lst, key),-1)

    def test_02(self):
        lst = [1,2,3,4]
        key = 1
        self.assertEqual(binary_search(lst, key),0)

    def test_03(self):
        lst = [1,2,3,4]
        key = -1
        self.assertEqual(binary_search(lst, key),-1)

    def test_04(self):
        lst = [1,2,3,4]
        key = 4
        self.assertEqual(binary_search(lst, key),3)

  
if __name__ == '__main__':
    unittest.main(verbosity=2)
