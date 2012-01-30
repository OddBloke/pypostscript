class AllIntegerArgumentShape(object):
    """
    A class which takes only integer arguments during init.

    """
    def __init__(self, *args):
        for arg in args:
            if not (isinstance(arg, int) and arg >= 0):
                raise ValueError(arg)


class Circle(AllIntegerArgumentShape):
    """
    Generic representation of a circle.

    """
    def __init__(self, x_pts, y_pts, radius_pts, line_width_pts):
        super(Circle, self).__init__(x_pts, y_pts, radius_pts, line_width_pts)

        self.x_pts, self.y_pts, self.radius_pts, self.line_width_pts = \
            x_pts, y_pts, radius_pts, line_width_pts

    @property
    def ps(self):
        """
        PostScript string representation of this object.

        """
        return ('newpath {x_pts} {y_pts} {radius_pts} 0 360 arc\n'
                'closepath\n'
                '{line_width_pts} setlinewidth\n'
                'stroke\n'.format(x_pts=self.x_pts,
                                  y_pts=self.y_pts,
                                  radius_pts=self.radius_pts,
                                  line_width_pts=self.line_width_pts))


class Rectangle(AllIntegerArgumentShape):
    """
    Generic representation of a rectangle.

    """
    def __init__(self, x_pts, y_pts, width_pts, height_pts, line_width_pts):
        super(Rectangle, self).__init__(x_pts, y_pts, width_pts, height_pts,
                                        line_width_pts)

        self.x_pts, self.y_pts, self.width_pts, \
        self.height_pts, self.line_width_pts = \
            x_pts, y_pts, width_pts, height_pts, line_width_pts

    @property
    def ps(self):
        """
        PostScript string representation of this object.

        """
        return ('newpath {x_pts} {y_pts} moveto\n'
                '{width_pts_pos} 0 rlineto\n'
                '0 {height_pts_pos} rlineto\n'
                '{width_pts_neg} 0 rlineto\n'
                '0 {height_pts_neg} rlineto\n'
                'closepath\n'
                '{line_width_pts} setlinewidth\n'
                'stroke\n'.format(
                    x_pts=self.x_pts,
                    y_pts=self.y_pts,
                    height_pts_pos=self.height_pts,
                    height_pts_neg=(self.height_pts * -1),
                    width_pts_pos=self.width_pts,
                    width_pts_neg=(self.width_pts * -1),
                    line_width_pts=self.line_width_pts))
