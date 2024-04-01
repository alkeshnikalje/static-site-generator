class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag if tag is not None else ""
        self.value = value if value is not None else ""
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):

        raise NotImplementedError()
    
    def props_to_html(self):

        if not self.props:
            return ""

        html_attrs = ' '.join(f'{key}="{value}"' for key,value in self.props.items())

        return f' {html_attrs}'
    
    def __repr__(self):

        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"