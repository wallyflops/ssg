from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError
        if children is None: 
            raise ValueError
        
        value=None
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag found")
        if self.children is None:
            raise ValueError("No children found")

        str_builder = ''
        for x in self.children:
            str_builder += x.to_html()
        
        strb = f"<{self.tag}>{str_builder}</{self.tag}>"

        return strb




    