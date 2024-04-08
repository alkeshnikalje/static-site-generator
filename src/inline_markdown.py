from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes,delimeter,text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimeter)
            nodes = []
            if len(split_nodes) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            for i in range(len(split_nodes)):
                if split_nodes[i] != "":

                    if i % 2 == 0:
                        nodes.append(TextNode(split_nodes[i],"text"))
                    else:
                        nodes.append(TextNode(split_nodes[i], text_type))
                        
            new_nodes.extend(nodes)
    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            text_to_be_processed = node.text
            for match in matches:
                delimter = f"![{match[0]}]({match[1]})"
                split_text = text_to_be_processed.split(delimter,1)
                if split_text[0]:
                    new_nodes.append(TextNode(split_text[0],"text"))
                new_nodes.append(TextNode(match[0],"image",match[1]))
                if len(split_text) > 1:
                    text_to_be_processed = split_text[1]
            if text_to_be_processed:
                new_nodes.append(TextNode(text_to_be_processed,"text"))
    return new_nodes
