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

    html_node = HtmlNode(props=input)
    # a = html_node.props_to_html()
    # print(a)
    
    # print(html_node)
    # leaf_node = LeafNode(tag=None, value='Heres a stringaling')
    # leaf_node_2 = LeafNode(tag='p', value='Heres a stringaling')
    # leaf_node_3 = LeafNode(tag='a', value='"Click me!", {"href": "https://www.google.com"}')
    # a = leaf_node.to_html()
    # b = leaf_node_2.to_html()
    # c = leaf_node_3.to_html()
    
    # print(c)
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

    text_node = TextNode("This is a test", TextType.NORMAL)
    text_node_2 = TextNode("This is a test", TextType.LINK)

    b = text_node_2.text_node_to_html_node()
    print(b)

if __name__ == "__main__":
    main()

