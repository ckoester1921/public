from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINKS = "Links"
    IMAGES = "Images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text).to_html()
            case TextType.BOLD:
                return LeafNode("b", self.text).to_html()
            case TextType.ITALIC:
                return LeafNode("i", self.text).to_html()
            case TextType.CODE:
                return LeafNode("code", self.text).to_html()
            case TextType.LINKS:
                return LeafNode("a", self.text, {"href": self.url}).to_html()
            case TextType.IMAGES:
                return LeafNode("img", "", {"src": self.url, "alt": self.text}).to_html()
            case _:
                raise ValueError(f"Invalid text type: {self.text_type}")
