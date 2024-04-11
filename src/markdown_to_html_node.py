from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
)
def block_to_html_node(block,block_type):
    if block_type == block_type_heading:
        pass

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def block_to_htmlnode_heading(block):
    heading = 0
    for i in block:
        if i == "#":
            heading += 1
        else:
            break
    if heading > 6 or heading+1 > len(block):
        raise ValueError(f"heading level {heading} is invalid")
    text = block[heading+1:len(block)]
    children = text_to_children(text)
    return ParentNode(f"h{heading}", children)
