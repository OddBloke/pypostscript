from re import match

from pypostscript import AllIntegerArgumentClass


class Barcode(AllIntegerArgumentClass):

    required_parts = ['barcode']

    def __init__(self, x_pts, y_pts, chars):

        super(Barcode, self).__init__(x_pts, y_pts)

        if not match(r'^[A-Z0-9]+$', chars):
            raise ValueError(chars)

        self._x_pts, self._y_pts, self._chars = \
            x_pts, y_pts, chars

    @property
    def ps(self):
        return ('{x_pts} {y_pts} moveto ({chars}) '
                '(includecheck includetext)\n'
                '/{barcode_code} /uk.co.terryburton.bwipp '
                'findresource exec\n'.format(
                    x_pts=self._x_pts,
                    y_pts=self._y_pts,
                    chars=self._chars,
                    barcode_code=self.BARCODE_CODE))


class Code39Barcode(Barcode):

    BARCODE_CODE = 'code39'


class Code93Barcode(Barcode):

    BARCODE_CODE = 'code93'
