class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string_builder = ''
        for prop, y in self.props.items():
            string_builder += f" {prop}=\"{y}\""
        return string_builder

    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"