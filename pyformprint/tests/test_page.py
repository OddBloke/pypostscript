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
        page.extend(circle)
        self.assertEqual(page.ps,
                         circle.ps)

    def test_page_many_shapes(self):
        """
        Shapes appended to Page should have their ps rendered correctly.

        """
        circle_1 = Circle(x_pts=50,
                          y_pts=100,
                          radius_pts=50,
                          line_width_pts=2)
        rectangle_1 = Rectangle(x_pts=300,
                                y_pts=300,
                                height_pts=50,
                                width_pts=75,
                                line_width_pts=5)
        circle_2 = Circle(x_pts=150,
                          y_pts=200,
                          radius_pts=20,
                          line_width_pts=3)
        rectangle_2 = Rectangle(x_pts=100,
                                y_pts=100,
                                height_pts=5,
                                width_pts=37,
                                line_width_pts=1)
        page = Page()
        page.extend(circle_1, rectangle_1, circle_2, rectangle_2)
        self.assertEqual(page.ps,
                         '\n'.join([shape.ps for shape in (circle_1,
                                                           rectangle_1,
                                                           circle_2,
                                                           rectangle_2)]))

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
