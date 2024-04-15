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
      
      with open(dest_path, 'w') as destination_file:
        destination_file.write(replaced)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  pass