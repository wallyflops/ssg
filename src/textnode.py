from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = ""
    BOLD = "**"
    ITALIC = ""
    CODE = "`"
    LINK = ""
    IMAGE = ""

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, TextNode):
        return (self.text == TextNode.text 
        and self.text_type == TextNode.text_type 
        and self.url == self.url )

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=self.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=self.text)
            case TextType.LINK:
                return LeafNode(tag="a", value=self.text, props="href")
            case TextType.IMAGE:
                return LeafNode(tag="img", value=self.text)
            case _:
                raise Exception("wrong type")
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
