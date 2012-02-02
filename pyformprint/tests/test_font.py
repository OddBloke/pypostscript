from decimal import Decimal
from unittest2 import TestCase

from pyformprint.text import (HelveticaBoldFont, HelveticaPlainFont,
                              TimesBoldFont, TimesPlainFont)


class TimesPlainFontTestCase(TestCase):

    def test_times_plain_font(self):
        """
        TimesPlainFont should render correct ps.

        """
        times_plain_font = TimesPlainFont(size_pts=23)
        self.assertEqual(times_plain_font.ps,
                         '/Times-Roman findfont\n'
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


class TimesBoldFontTestCase(TestCase):

    def test_times_bold_font(self):
        """
        TimesBoldFont should render correct ps.

        """
        times_bold_font = TimesBoldFont(size_pts=71)
        self.assertEqual(times_bold_font.ps,
                         '/Times-Bold findfont\n'
                         '71 scalefont\n'
                         'setfont\n')

    def test_times_bold_font_valitaion(self):
        """
        Bad size_pts in TimesBoldFont should raise error.

        """
        for bad_size_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                TimesBoldFont,
                size_pts=bad_size_pts)


class HelveticaPlainFontTestCase(TestCase):

    def test_helv_plain_font(self):
        """
        HelveticaPlainFont should render correct ps.

        """
        helv_plain_font = HelveticaPlainFont(size_pts=15)
        self.assertEqual(helv_plain_font.ps,
                         '/Helvetica findfont\n'
                         '15 scalefont\n'
                         'setfont\n')

    def test_helv_plain_font_valitaion(self):
        """
        Bad size_pts in HelveticaPlainFont should raise error.

        """
        for bad_size_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                HelveticaPlainFont,
                size_pts=bad_size_pts)


class HelveticaBoldFontTestCase(TestCase):

    def test_helv_bold_font(self):
        """
        HelveticaBoldFont should render correct ps.

        """
        helv_bold_font = HelveticaBoldFont(size_pts=8)
        self.assertEqual(helv_bold_font.ps,
                         '/Helvetica-Bold findfont\n'
                         '8 scalefont\n'
                         'setfont\n')

    def test_helv_bold_font_valitaion(self):
        """
        Bad size_pts in HelveticaBoldFont should raise error.

        """
        for bad_size_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                HelveticaBoldFont,
                size_pts=bad_size_pts)

# Tests needed
"""
    TextLine object

    TextBox object

    Line wrapping awareness (Paragraph object)

    Handle breaks in text - paragraph set or TextBox with Paragraphs in it

    "document" which uses the .ps property of all components if required

    "@uselib('barcodes')" should put the barcode lib into the top of the output
    document

    group all equivalent font/size combinations in the same block for document
"""
