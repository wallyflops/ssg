from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = ""
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, props=None):
        self.text = text
        self.text_type = text_type
        self.props = props
    
    def __eq__(self, TextNode):
        return (self.text == TextNode.text 
        and self.text_type == TextNode.text_type 
        and self.props == self.props )

    def text_node_to_html_node(self):
        print(f"selftexttype: {self.text_type}")
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=self.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=self.text)
            case TextType.LINK:
                return LeafNode(tag="a", value=self.text, props=self.props)
            case TextType.IMAGE:
                return LeafNode(tag="img", value="", props=self.props)
            case _:
                raise Exception("wrong type")
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.props})"
