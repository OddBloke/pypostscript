class TimesPlainFont(object):
    def __init__(self, size_pts):
        """
        Generic representation of a Times Roman font.

        """
        if not (isinstance(size_pts, int) and size_pts > 0):
            raise ValueError(size_pts)

        self.size_pts = size_pts

    @property
    def ps(self):
        """
        PostScript string representation of this object.

        """
        return ('/Times-Roman findfont\n'
                '{size_pts} scalefont\n'
                'setfont\n'.format(size_pts=self.size_pts))


class TimesBoldFont(object):
    def __init__(self, size_pts):
        """
        Generic representation of a Times Bold font.

        """
        if not (isinstance(size_pts, int) and size_pts > 0):
            raise ValueError(size_pts)

        self.size_pts = size_pts

    @property
    def ps(self):
        """
        PostScript string representation of this object.

        """
        return ('/Times-Bold findfont\n'
                '{size_pts} scalefont\n'
                'setfont\n'.format(size_pts=self.size_pts))
