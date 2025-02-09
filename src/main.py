from textnode import TextNode, TextType
from htmlnode import HtmlNode
from leafnode import LeafNode

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
    leaf_node = LeafNode(tag=None, value='Heres a stringaling')
    leaf_node_2 = LeafNode(tag='p', value='Heres a stringaling')
    leaf_node_3 = LeafNode(tag='a', value='"Click me!", {"href": "https://www.google.com"}')
    a = leaf_node.to_html()
    b = leaf_node_2.to_html()
    c = leaf_node_3.to_html()
    
    print(c)

if __name__ == "__main__":
    main()

