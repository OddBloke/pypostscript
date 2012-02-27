# -*- coding: utf-8 -*-
from unittest2 import TestCase

from pyformprint.barcode import Code39Barcode, Code93Barcode


class Code39BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        Code39Barcode should have 'barcode' in required_parts and render ps.

        """
        barcode = Code39Barcode(x_pts=30,
                                y_pts=500,
                                chars='CODE39TEST')
        self.assertIn('barcode', barcode.required_parts)
        self.assertEqual(
            barcode.ps,
            '30 500 moveto (CODE39TEST) (includecheck includetext)\n'
            '/code39 /uk.co.terryburton.bwipp findresource exec\n')


class Code93BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        Code93Barcode should have 'barcode' in required_parts and render ps.

        """
        barcode = Code93Barcode(x_pts=300,
                                y_pts=50,
                                chars='CODE93TEST')
        self.assertIn('barcode', barcode.required_parts)
        self.assertEqual(
            barcode.ps,
            '300 50 moveto (CODE93TEST) (includecheck includetext)\n'
            '/code93 /uk.co.terryburton.bwipp findresource exec\n')


class BarcodeTestCase(TestCase):

    def test_barcode_bad_chars(self):
        """
        Barcode should reject anything other than uppercase / base ASCII.

        """
        self.assertRaises(ValueError,
                          Code39Barcode,
                          x_pts=30,
                          y_pts=500,
                          chars='ickleletters')
        self.assertRaises(ValueError,
                          Code39Barcode,
                          x_pts=30,
                          y_pts=500,
                          chars='A SPACE')
        self.assertRaises(ValueError,
                          Code39Barcode,
                          x_pts=30,
                          y_pts=500,
                          chars='CORRIGÉ')


# Tests needed
"""
    portrait / landscape layout

    text box

    Functional tests that produce PostScript that can be loaded elsewhere:

        - portrait / landscape with simple shapes + text lines

        - portrait / landscape with barcode

        - portrait / landscape with textbox

        - portrait / landscape with barcode and textbox
"""
