from unittest2 import TestCase

from mock import Mock, patch

from pyformprint.page import Page
from pyformprint.shapes import Circle, Rectangle
from pyformprint.text import TextLine, TimesBoldFont


class PageTestCase(TestCase):

    def test_page_one_object(self):
        """
        Object appended to Page should render in its body.

        """
        circle = Circle(x_pts=50,
                        y_pts=100,
                        radius_pts=50,
                        line_width_pts=2)

        page = Page()
        page.extend(circle)
        self.assertEqual(page.body(),
                         circle.ps)

    def test_page_many_objects(self):
        """
        Objects appended to Page should render in its body.

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
        text_line = TextLine(x_pts=250,
                             y_pts=210,
                             font=TimesBoldFont(size_pts=18),
                             text='Some Text')
        page = Page()
        page.extend(circle_1, rectangle_1, circle_2, rectangle_2, text_line)
        self.assertEqual(page.body(),
                         '\n'.join([shape.ps for shape in (circle_1,
                                                           rectangle_1,
                                                           circle_2,
                                                           rectangle_2,
                                                           text_line)]))

    @patch('pyformprint.page.Page.footer')
    @patch('pyformprint.page.Page.body')
    @patch('pyformprint.page.Page.header')
    def test_page_render_composition(self, header, body, footer):
        """
        Page render() method should produce composed output.

        """
        header.return_value, body.return_value, footer.return_value = \
            'HEADER', 'BODY', 'FOOTER'

        page = Page()
        self.assertEqual(page.render(), 'HEADERBODYFOOTER')

    @patch('pyformprint.page.Page.read_part')
    @patch('pyformprint.page.Page.PAGE_START_PART', 'PAGE_START_PART')
    def test_header_simple(self, read_part):
        """
        header() should only read page start part if no requires_headers.

        """
        read_part.return_value = 'part_0'
        page = Page()
        header = page.header()
        self.assertEqual(read_part.call_args_list,
                         [(tuple(), {'name': 'PAGE_START_PART'})])
        self.assertEqual(header,
                         'part_0\n')

    @patch('pyformprint.page.Page.read_part')
    @patch('pyformprint.page.Page.PAGE_START_PART', 'PAGE_START_PART')
    def test_header_include_parts(self, read_part):
        """
        Page.header() should call read_part for appropriate parts.

        """
        read_part.side_effect = ['part_0', 'part_1', 'part_2', 'part_3']
        page = Page()
        ps_object_1 = Mock()
        ps_object_1.required_parts = ['foo']
        ps_object_2 = Mock()
        ps_object_2.required_parts = ['foo', 'bar', 'bang']
        page.extend(ps_object_1, ps_object_2)
        header = page.header()
        # Access to parts is unordered, strictly speaking
        parts_requested = [kwargs['name'] for args, kwargs in
                            read_part.call_args_list]
        self.assertEqual(len(parts_requested), 4)  # No repeat requests
        self.assertEqual(set(parts_requested),
                         set(['PAGE_START_PART', 'foo', 'bar', 'bang']))
        self.assertEqual(header,
                         'part_0\n'
                         'part_1\n'
                         'part_2\n'
                         'part_3\n')

    @patch('pyformprint.page.Page.read_part')
    @patch('pyformprint.page.Page.PAGE_END_PART', 'PAGE_END_PART')
    def test_footer(self, read_part):
        """
        footer() should read page end part.

        """
        read_part.return_value = 'part_99'
        page = Page()
        header = page.footer()
        self.assertEqual(read_part.call_args_list,
                         [(tuple(), {'name': 'PAGE_END_PART'})])
        self.assertEqual(header,
                         'part_99')  # No newline at end of file
