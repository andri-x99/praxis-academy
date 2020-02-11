import unittest
from kasusinsertion import insertion_sort as ins

class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        select = [3,4,5,8,9,10]
        self.assertEqual(select,ins([9,5,4,8,3,10]),"done")
        
    
if __name__ == '__main__':
    unittest.main()

# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)