# -*- coding: utf-8 -*-
from decimal import Decimal
from unittest2 import TestCase

from pypostscript.text import HelveticaPlainFont, TextLine


class TextLineTestCase(TestCase):

    def test_text_line_render_simple(self):
        """
        TextLine should render correct ps for simple text.

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

    def test_text_line_escapes_parentheses(self):
        """
        TextLine should escape parentheses in ps output.

        """
        helv_font = HelveticaPlainFont(size_pts=12)
        text_line = TextLine(x_pts=300, y_pts=200, font=helv_font,
                             text='I am a line of text (really).')
        self.assertEqual(text_line.ps,
                         '/Helvetica findfont\n'
                         '12 scalefont\n'
                         'setfont\n'
                         'newpath\n'
                         '300 200 moveto\n'
                         '(I am a line of text \(really\).) show\n')

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

    def test_text_line_reject_non_plain_ascii(self):
        """
        TextLine should reject anything other than basic ASCII (32-127).

        This is because in the base PostScript fonts, so-called "international"
        support is not guaranteed.

        """
        helv_font = HelveticaPlainFont(size_pts=12)

        for suspect_char in '\r\nü枇杷':
            print suspect_char
            self.assertRaises(ValueError,
                          TextLine,
                          x_pts=123,
                          y_pts=422,
                          font=helv_font,
                          text=suspect_char)

    def test_text_line_allow_plain_ascii(self):
        """
        TextLine should accept all normal basic ASCII (32-127).

        """
        helv_font = HelveticaPlainFont(size_pts=12)

        for char_ord in range(32, 128):
            char = chr(char_ord)

            # Brackets will complicate the test
            if char in '()':
                continue

            text_line = TextLine(x_pts=123,
                                 y_pts=422,
                                 font=helv_font,
                                 text=char)
            self.assertIn('({char}) show\n'.format(char=char),
                          text_line.ps)
