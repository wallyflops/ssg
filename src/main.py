from textnode import TextNode, TextType
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    # a = TextNode("text", TextType.BOLD, "http://blah.com")
    # print(a)
    input = {
        "href": "https://www.google.com/",
        "target": "_blank"
    }

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    a = node.to_html()

    # text_node = TextNode("This is a test", TextType.NORMAL)
    text_node_2 = TextNode("Some alt text", TextType.IMAGE, props={"src": "https://example.com/image.jpg", "alt": "Some alt text"})
    b = text_node_2.text_node_to_html_node()
    print(b)
    

    # Example of creating a link TextNode
    text_node_link = TextNode("Click me", TextType.LINK, props={"href": "https://www.google.com"})
    c = text_node_link.text_node_to_html_node()
    print(c)

if __name__ == "__main__":
    main()

