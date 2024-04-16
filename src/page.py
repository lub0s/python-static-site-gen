import os

from markdown import markdown_to_html_node
from markdown import extract_title


def generate_page(from_path, template_path, dest_path):
  print(f'Generating page from {from_path} to {dest_path} using {template_path}')

  with open(from_path, 'r') as markdown_file:
    with open(template_path, 'r') as template_file:
      markdown = markdown_file.read()
      template = template_file.read()

      html = markdown_to_html_node(markdown).to_html()
      title = extract_title(markdown)

      replaced = template.replace("""{{ Title }}""", title).replace("""{{ Content }}""", html)

      if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

      new_dst = _replace_file_ext(dest_path)
      with open(new_dst, 'w') as destination_file:
        destination_file.write(replaced)

def _replace_file_ext(file_path, new_extension='.html'):
  dir, filename = os.path.split(file_path)
  filename_without_ext, old_extension = os.path.splitext(filename)
  return os.path.join(dir, filename_without_ext + new_extension)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   dirs_and_files = os.listdir(dir_path_content)

   for entry in dirs_and_files:
     entry_path = os.path.join(dir_path_content, entry)
     dest_path = os.path.join(dest_dir_path, entry)

     if os.path.isdir(entry_path):
       generate_pages_recursive(entry_path, template_path, dest_path)
     else:
       generate_page(entry_path, template_path, dest_path)
