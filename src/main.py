
from copystatic import copy_file_contents
from generate_content import generate_pages_recursive
static_dir = "./static"
public_dir = "./public"

content_path = "./content"
template_path = "./template.html"


def main():

    print("Copying static files to public directory...")
    copy_file_contents(static_dir,public_dir)


    generate_pages_recursive(content_path,template_path,public_dir)
    


main()