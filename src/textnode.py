from htmlnode import HTMLNode
from leafnode import LeafNode

class TextNode:
  def __init__(self, text, text_type, url = None):
    self.text = text
    self.text_type = text_type
    self.url = url
  
  def to_html(self):
    if self.text_type == "text": return LeafNode(None, self.text)
    if self.text_type == "bold": return LeafNode("b", self.text)
    if self.text_type == "italic": return LeafNode("i", self.text)
    if self.text_type == "code": return LeafNode("code", self.text)
    if self.text_type == "link": return LeafNode("b", self.text, { "href": self.href  })
    if self.text_type == "image": return LeafNode("img", None, { "src" : self.href, "alt": self.text})
    else: raise Exception(f"unknown text_type: {self.text_type}")

  def __eq__(self, other):
    return self.text == other.text and self.text_type == other.text_type and self.url == other.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
    