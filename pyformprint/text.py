class Font(object):

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
        return ('/{ps_font_name} findfont\n'
                '{size_pts} scalefont\n'
                'setfont\n'.format(ps_font_name=self.PS_FONT_NAME,
                                   size_pts=self.size_pts))


class TimesPlainFont(Font):
    PS_FONT_NAME = 'Times-Roman'


class TimesBoldFont(Font):
    PS_FONT_NAME = 'Times-Bold'


class HelveticaPlainFont(Font):
    PS_FONT_NAME = 'Helvetica'


class HelveticaBoldFont(Font):
    PS_FONT_NAME = 'Helvetica-Bold'
