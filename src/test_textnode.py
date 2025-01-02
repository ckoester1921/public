import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, Normal text, https://www.boot.dev)", repr(node)
        )

    def test_text_to_html_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual("<b>This is bold text</b>", node.text_node_to_html_node())

    def test_text_to_html_link(self):
        node = TextNode("Go to Boot.dev", TextType.LINKS, "www.boot.dev")
        self.assertEqual('<a href="www.boot.dev">Go to Boot.dev</a>', node.text_node_to_html_node())

    def test_text_to_html_image(self):
        node = TextNode("Picture of a bear in a wizard hat", TextType.IMAGES, "www.boot.dev")
        self.assertEqual('<img src="www.boot.dev" alt="Picture of a bear in a wizard hat"></img>', node.text_node_to_html_node())


if __name__ == "__main__":
    unittest.main()