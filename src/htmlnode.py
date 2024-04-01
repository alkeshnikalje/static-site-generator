class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
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
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):

        if not self.value:
            raise ValueError("Leafnode should have a value")

        if not self.tag:
            return self.value
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        html_attrs = super().props_to_html()
        print("HTML attributes in to_html:", html_attrs)
        return f'<{self.tag}{html_attrs}>{self.value}</{self.tag}>'
