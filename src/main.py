from textnode import TextNode
from htmlnode import HTMLNode

def main():
    obj1 = TextNode("this is textnode", "bold", "https://www.boot.dev")
    print(obj1)

    html_node_obj = HTMLNode("h1","this is html node object")
    print(html_node_obj)
main()