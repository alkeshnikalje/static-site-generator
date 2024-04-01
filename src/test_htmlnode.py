import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        html_node = HTMLNode("h1","this is the h1 text")
        self.assertEqual("HTMLNode(h1,this is the h1 text,[],{})",repr(html_node))

    def test_props_to_html(self):
        html_node = HTMLNode("a","backend",[],{"href": "https://www.google.com", "target": "_blank"})
        expected_html = ' href="https://www.google.com" target="_blank"'
        actual_html = html_node.props_to_html()
        self.assertEqual(expected_html,actual_html)




if __name__ == "__main__":
    unittest.main()