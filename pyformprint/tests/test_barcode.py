# -*- coding: utf-8 -*-
from unittest2 import TestCase

from pyformprint.barcode import Code39Barcode, ITF14Barcode


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


class ITF14BarcodeTestCase(TestCase):

    def test_barcode(self):
        """
        ITF14Barcode should have 'barcode' in required_parts and render ps.

        """
        barcode = ITF14Barcode(x_pts=300,
                               y_pts=50,
                               chars='ITF14TEST')
        self.assertIn('barcode', barcode.required_parts)
        self.assertEqual(
            barcode.ps,
            '300 50 moveto (ITF14TEST) (includecheck includetext)\n'
            '/itf14 /uk.co.terryburton.bwipp findresource exec\n')


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
"""
