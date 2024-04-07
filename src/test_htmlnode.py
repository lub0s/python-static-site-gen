import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_props_to_html(self):
    htmlnode = HTMLNode("image", None, None, {"href": "https://www.google.com", "target": "_blank"})
    expected = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(htmlnode.props_to_html(), expected)
