from textnode import TextNode, TextType
from htmlnode import HtmlNode

def main():
    # a = TextNode("text", TextType.BOLD, "http://blah.com")
    # print(a)
    input = {
        "href": "https://www.google.com/",
        "target": "_blank"
    }

    html_node = HtmlNode(props=input)
    html_node.props_to_html()

if __name__ == "__main__":
    main()

