from textnode import TextNode
from leafnode import LeafNode

def main():
  print(f"{TextNode("This is a text node", "bold", "https://www.boot.dev")}")

def text_node_to_html_node(text_node):
  if text_node.text_type == "text_type_text":
    return LeafNode(None, text_node.text)
  if text_node.text_type == "text_type_bold":
    return LeafNode("b", text_node.text)
  if text_node.text_type == "text_type_italic":
    return LeafNode("i", text_node.text)
  if text_node.text_type == "text_type_code":
    return LeafNode("code", text_node.text)
  if text_node.text_type == "text_type_link":
    return LeafNode("b", text_node.text, { "href": text_node.href  })
  if text_node.text_type == "text_type_image":
    return LeafNode("img", text_node.text, None, { "src" : text_node.href, "alt": "alt text"})
  else: raise Exception(f"unknown text_type: {text_node.text_type}")

if __name__ == "__main__":
  main()
