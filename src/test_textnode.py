import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("asdasasd asd ", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", 
                        TextType.BOLD, 
                        props=None)
        node2 = TextNode("This is a text node", 
                        TextType.BOLD)
        
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("asdasasd asd ", TextType.BOLD)

        self.assertNotEqual(node, node3)
    
    def test_text_node_to_html_text(self):
        node = TextNode("testing plain text!", TextType.TEXT)
        node2 = node.text_node_to_html_node()

        self.assertEqual(node2.value, "testing plain text!")
    
    # def test_text_node


if __name__ == "__main__":
    unittest.main()