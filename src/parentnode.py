from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props = None):
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if self.tag == None: raise ValueError("Missing tag")
    inner = ""
    for child in self.children:
      inner += child.to_html()
    return f"<{self.tag}>{inner}</{self.tag}>"
