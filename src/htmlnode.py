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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    


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
