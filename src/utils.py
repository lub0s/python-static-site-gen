import re

from textnode import TextNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
  if not isinstance(text_node, TextNode): 
    raise Exception("Can only convert TextNode")
  return text_node.to_html()

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_list = []
  for old_node in old_nodes:
    if not isinstance(old_node, TextNode): 
      new_list.append(old_node) 
      continue
    # not sure about this
    if old_node.text_type != 'text': 
      new_list.append(old_node)
      continue
    splits = old_node.text.split(delimiter)

    if len(splits) == 1:
      new_list.append(TextNode(splits[0], "text"))
      continue

    if len(splits) == 2: 
      raise Exception(f"Might be missing closing tag! {len(splits)} {splits}")

    new_list.append(TextNode(splits[0], "text"))
    new_list.append(TextNode(splits[1], text_type))
    new_list.append(TextNode(splits[2], "text"))
  return new_list

def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
  result = []
  for node in old_nodes:
    if not isinstance(node, TextNode): raise Exception("not a TextNode")
    found = extract_markdown_images(node.text)
    if len(found) == 0: 
      result.append(node)
      continue
    rest_of_the_text = node.text
    for found_image in found:
      split = rest_of_the_text.split(f"![{found_image[0]}]({found_image[1]})", 1)[0]
      rest_of_the_text = rest_of_the_text.replace(split, "")
      rest_of_the_text = rest_of_the_text.replace(f"![{found_image[0]}]({found_image[1]})", "")
      result.append(TextNode(split, "text"))
      result.append(TextNode(found_image[0], "image", found_image[1]))
    if len(rest_of_the_text) != 0:
      result.append(TextNode(rest_of_the_text, 'text'))
  return result

def split_nodes_link(old_nodes):
  result = []
  for node in old_nodes:
    if not isinstance(node, TextNode): raise Exception("not a TextNode")
    found = extract_markdown_links(node.text)
    if len(found) == 0: 
      result.append(node)
      continue
    rest_of_the_text = node.text
    for found_link in found:
      split = rest_of_the_text.split(f"[{found_link[0]}]({found_link[1]})", 1)[0]
      rest_of_the_text = rest_of_the_text.replace(split, "")
      rest_of_the_text = rest_of_the_text.replace(f"[{found_link[0]}]({found_link[1]})", "")
      result.append(TextNode(split, "text"))
      result.append(TextNode(found_link[0], "link", found_link[1]))
    if len(rest_of_the_text) != 0:
      result.append(TextNode(rest_of_the_text, 'text'))
  return result

def text_to_textnodes(text):
  node = TextNode(text, 'text')
  nodes = [node]
  bolds = split_nodes_delimiter(nodes, '**', 'bold')
  italics = split_nodes_delimiter(bolds, '*', 'italic')
  codes = split_nodes_delimiter(italics, '`', 'code')
  images = split_nodes_image(codes)
  links = split_nodes_link(images)
  return links 

def text_to_htmlnodes(text):
  text_nodes = text_to_textnodes(text)
  return list(map(lambda tn: tn.to_html(), text_nodes))
