import os
import shutil



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