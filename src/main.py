
from copystatic import copy_file_contents,generate_page
static_dir = "./static"
public_dir = "./public"

def main():

    print("Copying static files to public directory...")
    copy_file_contents(static_dir,public_dir)

    generate_page("content/index.md","template.html","public/index.html")


main()