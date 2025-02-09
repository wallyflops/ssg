import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_lead_node_init(self):
        new_leaf = LeafNode(tag="a", value="Hello")

        tag = new_leaf.tag 
        print(tag)

        self.assertEqual(tag, "a")

    def test_lead_node_no_value(self):
        new_leaf = LeafNode(tag="a", value=None)

        self.assertRaises(ValueError)