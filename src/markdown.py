import re

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from block_types import block_type_paragraph
from block_types import block_type_code
from block_types import block_type_quote
from block_types import block_type_ulist
from block_types import block_type_list
from block_types import block_type_heading
from utils import text_to_textnodes
from utils import text_to_htmlnodes

def markdown_to_blocks(markdown):
  blocks = []
  splits = markdown.split('\n\n')
  for split in splits:
    blocks.append(split.lstrip().rstrip())
  return blocks

def block_to_block_type(markdown_block):
  # Headings start with 1-6 # characters
  if (markdown_block.startswith('# ') or
      markdown_block.startswith('## ') or
      markdown_block.startswith('### ') or
      markdown_block.startswith('#### ') or
      markdown_block.startswith('##### ') or
      markdown_block.startswith('###### ')
      ): return block_type_heading

  if markdown_block.startswith("```") and markdown_block.endswith('```'):
    return block_type_code

  lines = markdown_block.split('\n')

  if all(line.startswith('> ') for line in lines):
    return block_type_quote

  if all((line.startswith('*') or line.startswith('-')) for line in lines):
    return block_type_ulist

  is_list = False
  for line in range(0, len(lines)):
    is_list = lines[line].startswith(f'{line + 1}. ')

  if is_list:
    return block_type_list

  return block_type_paragraph

def heading_block_to_html_node(markdown):
  count = 0
  for char in markdown:
    if char == '#': count += 1
    else: break

  html_nodes = text_to_htmlnodes( markdown[count:].strip())
  return ParentNode(f'h{count}', html_nodes)

def code_block_to_html_node(markdown):
  stripped = markdown.lstrip('```').rstrip('```').strip()
  return ParentNode('pre', [LeafNode('code', stripped,)])

def quote_block_to_html_node(markdown):
  lines = list(map(lambda l: LeafNode('p',l.lstrip('> ')), markdown.split('\n')))
  return ParentNode('blockquote', lines)

def ul_block_to_html_node(markdown):
  children = []
  for line in markdown.split('\n'):
    children.append(ParentNode('li', text_to_htmlnodes(line.lstrip('* ').lstrip('- ').strip())))
  return ParentNode('ul', children)

def list_block_to_html_node(markdown):
  children = []
  for line in markdown.split('\n'):
    children.append(ParentNode('li', text_to_htmlnodes(re.sub(r'\b\d+\.', "", line).strip())))
  return ParentNode('ol', children)

def paragraph_block_to_html_node(markdown):
  html_nodes = text_to_htmlnodes(markdown)
  return ParentNode('p', html_nodes)

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)

  block_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)

    if block_type == block_type_heading:
      block_nodes.append(heading_block_to_html_node(block))
    elif block_type == block_type_code:
      block_nodes.append(code_block_to_html_node(block))
    elif block_type == block_type_quote:
      block_nodes.append(quote_block_to_html_node(block))
    elif block_type == block_type_ulist:
      block_nodes.append(ul_block_to_html_node(block))
    elif block_type == block_type_list:
      block_nodes.append(list_block_to_html_node(block))
    elif block_type == block_type_paragraph:
      block_nodes.append(paragraph_block_to_html_node(block))

  return ParentNode('div', block_nodes)

def extract_title(markdown):
  for line in markdown.split('\n'):
    if line.startswith('# '):
      return line.lstrip('# ').strip()
  raise Exception('All pages need a single h1 header.')
