from enum import Enum

class Textype(Enum):
    NORMAL_TEXT = "normal_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
       if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
           return True
       else:
           return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
