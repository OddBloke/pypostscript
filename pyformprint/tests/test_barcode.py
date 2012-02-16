from unittest2 import TestCase

from pyformprint.barcode import Code39Barcode


class Code39BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        Code39Barcode should have 'barcode' in requires_headers and render ps.

        """
        barcode = Code39Barcode(x_pts=30,
                                y_pts=500,
                                chars='Code 39 test')
        self.assertIn('barcode', barcode.requires_headers)
        self.assertEqual(
            barcode.ps,
            '30 500 moveto (Code 39 test) (includecheck includetext)\n'
            '/code39 /uk.co.terryburton.bwipp findresource exec\n')


# Tests needed
"""
    include barcode lib in Page if a barcode is in the mix

    barcode styles /code39 and /itf14

    chars in barcode should be limited to ascii

    portrait / landscape layout

    text box
"""
