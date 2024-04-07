import re

from textnode import TextNode
from utils import split_nodes_image

def main():
  node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    "text",
  )
  new_nodes = split_nodes_image([node])
  print(new_nodes)


if __name__ == "__main__":
  main()
