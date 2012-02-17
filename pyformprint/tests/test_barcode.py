from unittest2 import TestCase

from pyformprint.barcode import Code39Barcode, ITF14Barcode


class Code39BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        Code39Barcode should have 'barcode' in required_parts and render ps.

        """
        barcode = Code39Barcode(x_pts=30,
                                y_pts=500,
                                chars='Code 39 test')
        self.assertIn('barcode', barcode.required_parts)
        self.assertEqual(
            barcode.ps,
            '30 500 moveto (Code 39 test) (includecheck includetext)\n'
            '/code39 /uk.co.terryburton.bwipp findresource exec\n')


class ITF14BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        ITF14Barcode should have 'barcode' in required_parts and render ps.

        """
        barcode = ITF14Barcode(x_pts=300,
                               y_pts=50,
                               chars='ITF 14 TEST')
        self.assertIn('barcode', barcode.required_parts)
        self.assertEqual(
            barcode.ps,
            '300 50 moveto (ITF 14 TEST) (includecheck includetext)\n'
            '/itf14 /uk.co.terryburton.bwipp findresource exec\n')

# Tests needed
"""
    barcode styles /code39 and /itf14

    chars in barcode should be limited to ascii and uppercase / numerics only

    portrait / landscape layout

    text box
"""
