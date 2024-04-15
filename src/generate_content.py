import os
from markdown_to_html_node import markdown_to_html_node
from pathlib import Path


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")


def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path,"r") as f:
        template = f.read()
    
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content,entry)
        dest_path = os.path.join(dest_dir_path,entry)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path,template_path,dest_path)
        else:
            generate_pages_recursive(from_path,template_path,dest_path)