from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("Value must be populated")
        if tag == None:
            raise ValueError("tag must be populated")
        
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("There is no fucking value")
        if self.tag is None:
            return str(self.value)


