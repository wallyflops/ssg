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
        # print(string_builder)
        return string_builder