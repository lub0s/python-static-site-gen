from copy_dirs import copy_dirs
from page import generate_page

def main():
  copy_dirs('./static', './public')
  generate_page('./content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
  main()