from pyformprint import AllIntegerArgumentClass


class Code39Barcode(AllIntegerArgumentClass):

    required_parts = ['barcode']

    def __init__(self, x_pts, y_pts, chars):

        super(Code39Barcode, self).__init__(x_pts, y_pts)
        self._x_pts, self._y_pts, self._chars = \
            x_pts, y_pts, chars

    @property
    def ps(self):
        return ('{x_pts} {y_pts} moveto ({chars}) '
                '(includecheck includetext)\n'
                '/code39 /uk.co.terryburton.bwipp findresource exec\n'.format(
                    x_pts=self._x_pts,
                    y_pts=self._y_pts,
                    chars=self._chars))
