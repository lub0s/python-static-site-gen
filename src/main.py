from copy_dirs import copy_dirs
from page import generate_pages_recursive

def main():
  copy_dirs('./static', './public')
  generate_pages_recursive('./content', 'template.html', './public')

if __name__ == "__main__":
  main()