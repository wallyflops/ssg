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
        
        for x in self.children:
            print(f"x:::: {x.to_html()}")
        print(f"child: {self.children}")
        strb = f"<{self.tag}>"

        print(strb)

    # return a string representing the HTML tag of 
    # the node and its children. This should be a 
    # recursive method (each recursion being called on a 
    # nested child node). I iterated over all the children 
    # and called to_html on each, concatenating the 
    # results and injecting them between the opening 
    # and closing tags of the parent.




    