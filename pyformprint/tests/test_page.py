from unittest2 import TestCase

from pyformprint.page import Page
from pyformprint.shapes import Circle, Rectangle


class PageTestCase(TestCase):

    def test_page_one_shape(self):
        """
        Shape appended to Page should render its ps correctly.

        """
        circle = Circle(x_pts=50,
                        y_pts=100,
                        radius_pts=50,
                        line_width_pts=2)

        page = Page()
        page.append(circle)
        self.assertEqual(page.ps,
                         'newpath 50 100 50 0 360 arc\n'
                         'closepath\n'
                         '2 setlinewidth\n'
                         'stroke\n')

# Tests needed
"""
    "page" which uses the .ps property of all components if required

    "page" to include portrait/landscape setups

    "@uselib('barcodes')" should put the barcode lib into the top of the output
    document

    group all equivalent font/size combinations in the same block for document

    TextBox object

    Line wrapping awareness (Paragraph object)

    Handle breaks in text - paragraph set or TextBox with Paragraphs in it
"""
