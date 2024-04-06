from textnode import TextNode

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
            for i in len(split_nodes):
                if i % 2 == 0:
                    nodes.append(TextNode(split_nodes[i],"text"))
                else:
                    nodes.append(TextNode(split_nodes[i], text_type))
            new_nodes.extend(nodes)
    return new_nodes