import unittest

from textnode import TextNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from markdown import markdown_to_blocks
from markdown import block_to_block_type
import block_types 

class TestMarkdown(unittest.TestCase):

  def test_markdown_to_blocks(self):
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
      """

    blocks = markdown_to_blocks(markdown)

    self.assertEqual(len(blocks), 3)

  def test_block_to_block_type(self):
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
      """

    types = list(map(lambda block: block_to_block_type(block), markdown_to_blocks(markdown)))
    expected = [block_types.block_type_heading, block_types.block_type_paragraph, block_types.block_type_paragraph]

    self.assertEqual(types, expected)

  def test_markdown_to_html_node(self):
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
      """
      
      