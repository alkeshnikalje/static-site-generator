import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

print(extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"))