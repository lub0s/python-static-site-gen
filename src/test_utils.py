import unittest

from textnode import TextNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from utils import text_node_to_html_node
from utils import split_nodes_delimiter
from utils import extract_markdown_images
from utils import extract_markdown_links
from utils import split_nodes_image

class TestUtils(unittest.TestCase):

  def test_text_node_to_html_node(self):
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    expected = "HTMLNode(b, This is a text node, None, None)"

    self.assertEqual(f"{text_node_to_html_node(text_node)}", expected)

  def test_split_nodes_delimiter(self):
    code_node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([code_node], "`", "code")

    self.assertEqual(f"{new_nodes}", "[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]")

  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    extracted = extract_markdown_images(text)
    expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

    self.assertEqual(extracted, expected)

  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    extracted = extract_markdown_links(text)
    expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

    self.assertEqual(extracted, expected)

  def test_split_nodes_image(self):
    node = TextNode(
      "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
      "text",
    )
    new_nodes = split_nodes_image([node])
    expected = [TextNode("This is text with an ", "text", None), TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), TextNode(" and another ", "text", None), TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")]
    
    self.assertEqual(new_nodes, expected)
