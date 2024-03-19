import unittest
from BinnaryTreeLabs import successor, Node

class TestTreeFunctions(unittest.TestCase):
    def setUp(self):
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.right = Node(15)
        self.root.left.right = Node(7)
        self.root.left.left = Node(3)
        self.root.right.right = Node(20)
        self.root.right.right.left = Node(12)

    def test_find_successor(self):
        our_elem = self.root.left.right
        self.assertEqual(successor(self.root, our_elem), 10)

if __name__ == '__main__':
    unittest.main()
