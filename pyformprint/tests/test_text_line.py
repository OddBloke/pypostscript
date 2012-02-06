from decimal import Decimal
from unittest2 import TestCase

from pyformprint.text import HelveticaPlainFont, TextLine


class TextLineTestCase(TestCase):

    def test_text_line_render(self):
        """
        TextLine should render correct ps.

        """
        helv_font = HelveticaPlainFont(size_pts=12)
        text_line = TextLine(x_pts=300, y_pts=200, font=helv_font,
                             text='I am a line of text.')
        self.assertEqual(text_line.ps,
                         '/Helvetica findfont\n'
                         '12 scalefont\n'
                         'setfont\n'
                         'newpath\n'
                         '300 200 moveto\n'
                         '(I am a line of text.) show\n')

    def text_line(self):
        """
        Bad x_pts values in TextLine should raise error.

        """
        for bad_x_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                TextLine,
                x_pts=bad_x_pts,
                y_pts=396,
                font=HelveticaPlainFont(size_pts=12),
                text='well, this is lovely')

    def test_text_line_validation_y_pts(self):
        """
        Bad y_pts values in TextLine should raise error.

        """
        for bad_y_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                TextLine,
                x_pts=123,
                y_pts=bad_y_pts,
                font=HelveticaPlainFont(size_pts=12),
                text='well, this is lovely')

    def test_text_line_validation_font(self):
        """
        'font' argument of TextLine should be a Font object.

        """
        self.assertRaises(
                ValueError,
                TextLine,
                x_pts=123,
                y_pts=422,
                font='Helvetica',  # not a Font object
                text='well, this is lovely')


# Tests needed
"""
    brackets in textline?

    harder tests for textline, e.g. weird chars, foreign chars

    Refactor the Font base to be an all-integer class

    Inappropriate character sets in TextLine

    TextBox object

    Line wrapping awareness (Paragraph object)

    Handle breaks in text - paragraph set or TextBox with Paragraphs in it

    "document" which uses the .ps property of all components if required

    "@uselib('barcodes')" should put the barcode lib into the top of the output
    document

    group all equivalent font/size combinations in the same block for document
"""
