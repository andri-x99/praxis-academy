import unittest
from kasusquick import quick_sort as quick

class TestMerge(unittest.TestCase):
    def test_quick(self):
        q = [3,4,5,8,9,10]
        # self.assertEqual(q,quick([9,5,4,8,3,10]),"done")
        self.assertTrue(quick([9,5,4,8,3,10]) == q)
    
if __name__ == '__main__':
    unittest.main()

# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)