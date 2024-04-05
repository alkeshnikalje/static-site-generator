from textnode import TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode

def main():
    obj1 = TextNode("this is textnode", "bold", "https://www.boot.dev")
    print(obj1)

    html_node_obj = HTMLNode("h1","this is html node object",[], {"href": "example.com"})
    attrs = html_node_obj.props_to_html()
    print(attrs)
    leaf_node_obj = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    to_html = leaf_node_obj.to_html()
    print(to_html)
main()