from decimal import Decimal
from unittest2 import TestCase

from pyformprint.text import TimesPlainFont


class TimesPlainFontTestCase(TestCase):

    def test_times_plain_font(self):
        """
        TimesPlainFont should render correct ps.

        """
        times_plain_font = TimesPlainFont(size_pts=23)
        self.assertEqual(times_plain_font.ps,
                         '/Times-Bold findfont\n'
                         '23 scalefont\n'
                         'setfont\n')

    def test_times_plain_font_valitaion(self):
        """
        Bad size_pts in TimesPlainFont should raise error.

        """
        for bad_size_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                TimesPlainFont,
                size_pts=bad_size_pts)

# Tests needed
"""
    Font object

    TextLine object

    TextBox object

    Line wrapping awareness (Paragraph object)

    Handle breaks in text - paragraph set or TextBox with Paragraphs in it

    "document" which uses the .ps property of all components if required

    "@uselib('barcodes')" should put the barcode lib into the top of the output
    document

    group all equivalent font/size combinations in the same block for document
"""
