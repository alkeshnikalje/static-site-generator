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

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        child  = block_to_html_node(block,block_type)
        children.append(child)
    return ParentNode("div",children)

def block_to_html_node(block,block_type):
    if block_type == block_type_heading:
        return block_to_htmlnode_heading(block)
    if block_type == block_type_paragraph:
        return block_to_htmlnode_paragraph(block)
    if block_type == block_type_code:
        return block_to_htmlnode_code(block)
    if block_type == block_type_ordered_list:
        return block_to_htmlnode_ordered_list(block)
    if block_type == block_type_unordered_list:
        return block_to_htmlnode_unordered_list(block)
    if block_type == block_type_quote:
        return block_to_htmlnode_quote(block)

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
    if heading + 1 > len(block):
        raise ValueError(f"heading level {heading} is invalid")
    text = block[heading+1:len(block)]
    children = text_to_children(text)
    return ParentNode(f"h{heading}", children)

def block_to_htmlnode_paragraph(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p",children)


def block_to_htmlnode_code(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code",children)
    return ParentNode("pre",[code])

def block_to_htmlnode_ordered_list(block):
    list_items = block.split("\n")
    ol_children = []
    for item in list_items:
        if item == "":
            continue
        else:
            text = item[3:]
            children = text_to_children(text)
            ol_children.append(ParentNode("li",children))
    return ParentNode("ol",ol_children)

def block_to_htmlnode_unordered_list(block):
    list_items = block.split("\n")
    ul_children = []
    for item in list_items:
        if item == "":
            continue
        else:
            text = item[2:]
            children = text_to_children(text)
            ul_children.append(ParentNode("li",children))
    return ParentNode("ul",ul_children)

def block_to_htmlnode_quote(block):
    quote_lines = block.split("\n")
    text = ""
    for quote_line in quote_lines:
        if quote_line == "":
            continue
        else:
            text += quote_line[2:] + " "
    children = text_to_children(text[:-1])
    return ParentNode("blockquote", children)