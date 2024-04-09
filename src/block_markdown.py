def markdown_to_blocks(markdown):
    list_of_blocks = []
    for i in markdown.split("\n\n"):
        if i == "":
            continue
        list_of_blocks.append(i.strip())
    return list_of_blocks