import os
import shutil
from block_markdown import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node


def copy_file_contents(source_dir,destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    source_contents = os.listdir(source_dir)
    for item in source_contents:
        full_source_path = os.path.join(source_dir,item)
        full_dest_path = os.path.join(destination_dir,item)
        print(f" * {full_source_path} -> {full_dest_path}")
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path,full_dest_path)
        else:
            copy_file_contents(full_source_path,full_dest_path)

        
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
    print(title)
    new_template = template.replace("{{ Title }}",title)
    new_template = template.replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_template)