from decimal import Decimal
from unittest2 import TestCase

from pyformprint.shapes import Circle


class CircleTestCase(TestCase):

    def test_circle_draw(self):
        """
        Normal Circle should render correct ps.

        """
        circle = Circle(centre_x_pts=306, centre_y_pts=396, radius_pts=144,
                        line_width_pts=3)
        self.assertEqual(circle.ps,
                         'newpath 306 396 144 0 360 arc\n'
                         'closepath\n'
                         '3 setlinewidth\n'
                         'stroke\n')

    def test_circle_validation_centre_x_pts(self):
        """
        Bad centre_x_pts values in Circle should raise error.

        """
        for bad_x_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Circle,
                centre_x_pts=bad_x_pts,
                centre_y_pts=396,
                radius_pts=144,
                line_width_pts=3)

    def test_circle_validation_centre_y_pts(self):
        """
        Bad centre_y_pts values in Circle should raise error.

        """
        for bad_y_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Circle,
                centre_x_pts=306,
                centre_y_pts=bad_y_pts,
                radius_pts=144,
                line_width_pts=3)

    def test_circle_validation_radius_pts(self):
        """
        Bad radius_pts values in Circle should raise error.

        """
        for bad_radius_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Circle,
                centre_x_pts=306,
                centre_y_pts=396,
                radius_pts=bad_radius_pts,
                line_width_pts=3)

    def test_circle_validation_line_width_pts(self):
        """
        Bad line_width_pts values in Circle should raise error.

        """
        for bad_line_width_pts in (1.2, Decimal(3), -1, 'hello'):
            self.assertRaises(
                ValueError,
                Circle,
                centre_x_pts=306,
                centre_y_pts=396,
                radius_pts=144,
                line_width_pts=bad_line_width_pts)
