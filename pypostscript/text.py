import re

from pypostscript import AllIntegerArgumentClass


class Font(AllIntegerArgumentClass):
    """
    Generic representation of a Times Roman font.

    """
    def __init__(self, size_pts):
        super(Font, self).__init__(size_pts)

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


class TextLine(AllIntegerArgumentClass):
    """
    Generic representation of a line of text.

    """
    def __init__(self, x_pts, y_pts, font, text):
        if not isinstance(font, Font):
            raise ValueError(font)
        if not isinstance(text, basestring):
            raise ValueError(text)

        for char in text:
            char_ord = ord(char)
            if char_ord < 32 or char_ord > 127:
                raise ValueError(char)

        super(TextLine, self).__init__(x_pts, y_pts)

        self.x_pts, self.y_pts, self.font, self.text = \
            x_pts, y_pts, font, text

    @property
    def ps(self):
        """
        PostScript string representation of this object.

        """
        escaped_text = re.sub(r'([()])', r'\\\1', self.text)
        return (self.font.ps +
                    'newpath\n'
                    '{x_pts} {y_pts} moveto\n'
                    '({text}) show\n'.format(x_pts=self.x_pts,
                                             y_pts=self.y_pts,
                                             text=escaped_text))
