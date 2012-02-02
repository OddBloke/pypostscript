from decimal import Decimal
from unittest2 import TestCase

from pyformprint.shapes import Rectangle


class RectangleTestCase(TestCase):

    def test_rectangle_draw(self):
        """
        Normal Rectangle should render correct ps.

        """
        rectangle = Rectangle(x_pts=10, y_pts=40, width_pts=100,
                              height_pts=120, line_width_pts=5)
        self.assertEqual(rectangle.ps,
                         'newpath 10 40 moveto\n'
                         '100 0 rlineto\n'
                         '0 120 rlineto\n'
                         '-100 0 rlineto\n'
                         '0 -120 rlineto\n'
                         'closepath\n'
                         '5 setlinewidth\n'
                         'stroke\n')

    def test_rectangle_validation_x_pts(self):
        """
        Bad x_pts values in Rectangle should raise error.

        """
        for bad_x_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Rectangle,
                x_pts=bad_x_pts,
                y_pts=40,
                width_pts=100,
                height_pts=120,
                line_width_pts=5)

    def test_rectangle_validation_y_pts(self):
        """
        Bad y_pts values in Rectangle should raise error.

        """
        for bad_y_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Rectangle,
                x_pts=10,
                y_pts=bad_y_pts,
                width_pts=100,
                height_pts=120,
                line_width_pts=5)

    def test_rectangle_validation_width_pts(self):
        """
        Bad width_pts values in Rectangle should raise error.

        """
        for bad_width_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Rectangle,
                x_pts=10,
                y_pts=40,
                width_pts=bad_width_pts,
                height_pts=120,
                line_width_pts=5)

    def test_rectangle_validation_height_pts(self):
        """
        Bad height_pts values in Rectangle should raise error.

        """
        for bad_height_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Rectangle,
                x_pts=10,
                y_pts=40,
                width_pts=100,
                height_pts=bad_height_pts,
                line_width_pts=5)

    def test_rectangle_validation_line_width_pts(self):
        """
        Bad line_width_pts values in Rectangle should raise error.

        """
        for bad_line_width_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Rectangle,
                x_pts=10,
                y_pts=40,
                width_pts=100,
                height_pts=120,
                line_width_pts=bad_line_width_pts)
