import unittest
from kasusbubble2 import bubble_sort as s

class TestBubble(unittest.TestCase):
    def test_bubble1(self):
        bubble = [3,4,5,8,9]
        self.assertEqual(bubble,s([9,5,4,8,3]),"done")
        
    def test_bubble2(self):
        bubble = [3,4,5,8,9]
        self.assertTrue(s([9,5,4,8,3]) == bubble,"mantab pakde")
if __name__ == '__main__':
    unittest.main()

# random_list_of_nums = [5, 2, 1, 8, 4]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)