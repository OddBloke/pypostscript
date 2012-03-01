# coding=UTF-8
from os.path import dirname, join, split
from unittest2 import TestCase

from mock import Mock, patch

from pypostscript.page import A4PortraitPage, Page
from pypostscript.shapes import Circle, Rectangle
from pypostscript.text import TextLine, TimesBoldFont


class PageTestCase(TestCase):

    def test_PAGE_START_TEXT(self):
        """
        PAGE_START_TEXT needs to be provided in sub-classes.

        """
        with self.assertRaises(NotImplementedError):
            Page().PAGE_START_TEXT

    def test_from_text(self):
        """
        Page.from_text should set PAGE_START_TEXT.

        """
        x = Page.from_text('MockStartText')
        self.assertEqual('MockStartText', x.PAGE_START_TEXT)
        self.assertIsInstance(x(), Page)

    def test_page_one_object(self):
        """
        Object appended to Page should render in its body.

        """
        circle = Circle(centre_x_pts=50,
                        centre_y_pts=100,
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
        circle_1 = Circle(centre_x_pts=50,
                          centre_y_pts=100,
                          radius_pts=50,
                          line_width_pts=2)
        rectangle_1 = Rectangle(x_pts=300,
                                y_pts=300,
                                height_pts=50,
                                width_pts=75,
                                line_width_pts=5)
        circle_2 = Circle(centre_x_pts=150,
                          centre_y_pts=200,
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

    @patch('pypostscript.page.Page.footer')
    @patch('pypostscript.page.Page.body')
    @patch('pypostscript.page.Page.header')
    def test_page_render_composition(self, header, body, footer):
        """
        Page render() method should produce composed output.

        """
        header.return_value, body.return_value, footer.return_value = \
            'HEADER', 'BODY', 'FOOTER'

        page = Page()
        self.assertEqual(page.render(), 'HEADERBODYFOOTER')

    @patch('pypostscript.page.Page.read_part')
    @patch('pypostscript.page.Page.PAGE_START_TEXT', 'MockPageStart')
    def test_header_simple(self, read_part):
        """
        header() should output only page start text if no requires_headers.

        """
        page = Page()
        header = page.header()
        self.assertEqual(0, read_part.call_count)
        self.assertEqual(header,
                         'MockPageStart\n')

    @patch('pypostscript.page.Page.read_part')
    @patch('pypostscript.page.Page.PAGE_START_TEXT', 'MockPageStart')
    def test_header_include_parts(self, read_part):
        """
        Page.header() should call read_part for appropriate parts.

        """
        read_part.side_effect = ['part_1', 'part_2', 'part_3']
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
        self.assertEqual(len(parts_requested), 3)  # No repeat requests
        self.assertEqual(set(parts_requested),
                         set(['foo', 'bar', 'bang']))
        self.assertEqual(header,
                         'MockPageStart\n'
                         'part_1\n'
                         'part_2\n'
                         'part_3\n')

    @patch('pypostscript.page.Page.read_part')
    @patch('pypostscript.page.Page.PAGE_END_PART', 'page_end_part')
    def test_footer(self, read_part):
        """
        footer() should read page end part.

        """
        read_part.return_value = 'part_99'
        page = Page()
        header = page.footer()
        self.assertEqual(read_part.call_args_list,
                         [(tuple(), {'name': 'page_end_part'})])
        self.assertEqual(header,
                         'part_99')  # No newline at end of file

    @patch('pypostscript.page.open')
    @patch('pypostscript.page.Page.PARTS_DIR', 'parts_dir')
    def test_read_part(self, open_stmt):
        """
        read_part() should retrieve contents of given part file.

        """
        open_stmt.return_value.read.return_value = 'some file contents'
        page = Page()
        part = page.read_part(name='foo')
        self.assertEqual(part, 'some file contents')
        root_package_dir = split(split(dirname(__file__))[0])[0]
        expected_path = join(root_package_dir, 'parts_dir', 'foo')
        self.assertEqual(open_stmt.call_args_list,
                         [((expected_path, 'r'), {})])


class TestA4PortraitPage(TestCase):

    def test_PAGE_START_TEXT(self):
        """
        PAGE_START_TEXT should be correct.

        """
        self.assertEqual(
            "\n".join(
                ["%!PS−Adobe−2.0",
                 "%%BoundingBox: 0 0 595.28 841.89 % A4 %",
                 "%%Creator: pypostscript",
                 "%%EndComments",
                 ""]),
            A4PortraitPage.PAGE_START_TEXT)
