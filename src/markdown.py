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

def quote_block_to_html_node(markdown):
  return ParentNode('blockquote', [LeafNode(None, f"{markdown}")])
  
def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)

  block_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)
    
    if block_type == block_type_heading:
      block_nodes.append()
    elif block_type == block_type_code:
      block_nodes.append()
    elif block_type == block_type_quote:
      block_nodes.append(quote_block_to_html_node(block))
    elif block_type == block_type_ulist:
      block_nodes.append()
    elif block_type == block_type_list:
      block_nodes.append()
    elif block_type == block_type_paragraph:
      block_nodes.append()

  return ParentNode('div', block_nodes)
