block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    list_of_blocks = []
    for i in markdown.split("\n\n"):
        if i == "":
            continue
        list_of_blocks.append(i.strip())
    return list_of_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswtih("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") or not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1} "):
                return block_type_paragraph
        return block_type_ordered_list
    return block_type_paragraph

    