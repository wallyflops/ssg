import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_lead_node_init(self):
        new_leaf = LeafNode(tag="a", value="Hello")

        tag = new_leaf.tag 
        print(tag)

        self.assertEqual(tag, "a")

    def test_lead_node_no_value(self):
        with self.assertRaises(TypeError):  # Expect TypeError, not ValueError
            LeafNode(tag="a")

    def test_lead_node_none_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="a", value=None)
    
    def test_lead_node_tag_none(self):
        node = LeafNode(tag=None, value="Here's text")
        value = node.to_html()
        self.assertEqual(value, "Here's text")

    # def test_lead_node_with_value(self):
    #     node = LeafNode(tag="p", value="This is a paragraph of text.")
    #     node.to_html()

    #     self.assertEqual("<p>This is a paragraph of text.</p>")



