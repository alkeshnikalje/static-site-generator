import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("hello textnode", "bold")
        node2 = TextNode("hello textnode", "italic")
        self.assertEqual(node,node2)
    
    def test_eq_false2(self):
        node = TextNode("hello textnode1", "bold")
        node2 = TextNode("hello textnode2", "bold")
        self.assertEqual(node,node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", "italic", "https://www.boot.dev"
        )
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node,italic,https://www.boot.dev)", repr(node))

    def test_text_node_to_html_node(self):
        text_node = TextNode("click me!","link","https://www.google.com")
        text_node_to_leaf_node = text_node_to_html_node(text_node=text_node)
        self.assertEqual(LeafNode("a","click me!",{"href": "https://www.google.com"}),text_node_to_leaf_node)


if __name__ == "__main__":
    unittest.main()
