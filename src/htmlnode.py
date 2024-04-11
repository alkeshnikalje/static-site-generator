class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 
    
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
    
    def __eq__(self,other):
            return (
            isinstance(other, LeafNode) and
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )
    
    def to_html(self):

        if not self.value:
            raise ValueError("Leafnode should have a value")

        if not self.tag:
            return self.value
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        html_attrs = super().props_to_html()
        return f'<{self.tag}{html_attrs}>{self.value}</{self.tag}>'

    def __str__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag=None,children=None, props=None,):
        super().__init__(tag=tag,children=children,props=props)

    
    def to_html(self):
        
        if not self.tag:
            raise ValueError("ParentNode should have a an html tag")
        
        if not self.children:
            raise ValueError("parentNode should have at leaat one children")

        output = ""
        for child in self.children:
            res = child.to_html()
            output += res
        
        return f'<{self.tag}>{output}</{self.tag}>'
    
    def __str__(self):
        return f"ParentNode({self.tag},{self.children},{self.props})"
