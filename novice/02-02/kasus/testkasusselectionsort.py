import unittest
from kasusselectionsort import selection_sort as se

class TestBubble(unittest.TestCase):
    def test_selectionsort(self):
        select = [3,4,5,8,9]
        self.assertEqual(select,se([9,5,4,8,3]),"done")
        
    
if __name__ == '__main__':
    unittest.main()

# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)