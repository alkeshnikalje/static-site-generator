from htmlnode import LeafNode
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

def block_to_htmlnode_heading(block):
    heading = 0
    for i in block:
        if i == "#":
            heading += 1
        else:
            break
    new_block = block[heading+1:len(block)]
    if "**" not in block and "`" not in block and "*" not in new_block:
        return LeafNode(f"h{heading}",new_block)
    
print(block_to_htmlnode_heading("# My Blog Post"))