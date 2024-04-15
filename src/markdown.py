from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from block_types import block_type_paragraph
from block_types import block_type_code
from block_types import block_type_quote
from block_types import block_type_ulist
from block_types import block_type_list
from block_types import block_type_heading

def markdown_to_blocks(markdown):
  blocks = []
  splits = markdown.split('\n\n')
  for split in splits:
    blocks.append(split.lstrip().rstrip())
  return blocks

def block_to_block_type(markdown_block):
  # Headings start with 1-6 # characters
  if markdown_block.startswith('# '):
    return block_type_heading
  if markdown_block.startswith('## '):
    return block_type_heading
  if markdown_block.startswith('### '):
    return block_type_heading
  if markdown_block.startswith('#### '):
    return block_type_heading
  if markdown_block.startswith('##### '):
    return block_type_heading
  if markdown_block.startswith('###### '):
    return block_type_heading
  
  if markdown_block.startswith("```"):
    return block_type_code
  
  if all(line.startswith('>') for line in markdown_block.split()):
    return block_type_quote
  
  if all((line.startswith('*') or line.startswith('-')) for line in markdown_block.split()):
    return block_type_ulist
  
  is_list = False
  lines = markdown_block.split()
  for line in range(0, len(lines)):
    is_list = lines[line].startswith(f'{line + 1}. ')

  if is_list:
    return block_type_list
  
  return block_type_paragraph

def heading_block_to_html_node(markdown):
  # count
  # tag
  return LeafNode('h1', markdown)

def code_block_to_html_node(markdown):
  return ParentNode('pre', [LeafNode('code', markdown,)])

def quote_block_to_html_node(markdown):
  return LeafNode('blockquote', markdown)

def ul_block_to_html_node(markdown):
  children = []
  for line in markdown:
    children.append(LeafNode('li', line))
  return LeafNode('ul', children)

def list_block_to_html_node(markdown):
  children = []
  for line in markdown:
    children.append(LeafNode('li', line))
  return ParentNode('ol', children)
  
def paragraph_block_to_html_node(markdown):
  return LeafNode('p', markdown)
  
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
      return line
  raise Exception('All pages need a single h1 header.')
