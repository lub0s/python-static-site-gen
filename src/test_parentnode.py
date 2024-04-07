import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_a(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )

    expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    self.assertEqual(node.to_html(), expected)

  def test_b(self):
    node = ParentNode("p", [
      ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    ])

    expected = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
    self.assertEqual(node.to_html(), expected)