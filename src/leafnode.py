from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value must be populated")
        # if tag is None:
        #     raise ValueError("tag must be populated")
        
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("There is no fucking value")
        if self.tag is None:
            return str(self.value)

        if self.tag == "a":
            #TOOD use the props_to_html parent class???
            value_lst = self.value.split(",")
            value_txt = value_lst[0].replace('"', "")
            url = value_lst[1].split(": ")[1].replace("}", "")
            start = value_lst[1].split(": ")[0].replace('"', '').replace("{", "")

            return f"<{self.tag} {start}={url}>{value_txt}</{self.tag}>" 
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

