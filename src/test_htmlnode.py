import unittest
from htmlnode import HtmlNode

class TestHtmlNodeProps(unittest.TestCase):
    def test_props_to_html_google(self):
        input = {
            "href": "https://www.google.com/",
            "target": "_blank"
        }

        html_node = HtmlNode(props=input)

        output = " href=\"https://www.google.com/\" target=\"_blank\""
        ans = html_node.props_to_html()

        self.assertEqual(ans, output)

    def test_props_to_html_something(self):
        input = {
            "href": "https://www.shit.com/",
            "another": "_blank"
        }

        html_node = HtmlNode(props=input)

        output = " href=\"https://www.shit.com/\" another=\"_blank\""
        ans = html_node.props_to_html()

        self.assertEqual(ans, output)

    def test_props_to_html_idontknow(self):
        input = {
            "href": "https://www.idontknow.com/",
            "another": "_blank"
        }

        html_node = HtmlNode(props=input)

        output = " href=\"https://www.idontknow.com/\" another=\"_blank\""
        ans = html_node.props_to_html()

        self.assertEqual(ans, output)

if __name__ == "__main__":
    unittest.main()