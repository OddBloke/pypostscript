from pyformprint.barcode import Code39Barcode, Code93Barcode
from pyformprint.shapes import Circle, Rectangle
from pyformprint.text import HelveticaBoldFont, TextLine, TimesPlainFont
from pyformprint.page import Page


def sample_page():
    page = Page()
    page.extend(TextLine(x_pts=40,
                         y_pts=740,
                         font=HelveticaBoldFont(size_pts=22),
                         text='A Test Portrait Page'))
    page.extend(TextLine(x_pts=40,
                         y_pts=650,
                         font=TimesPlainFont(size_pts=12),
                         text='PostScript library, test portrait page.'))
    page.extend(Code39Barcode(x_pts=40,
                              y_pts=500,
                              chars='ABC123'))
    page.extend(Code93Barcode(x_pts=40,
                              y_pts=400,
                              chars='ABC987'))
    page.extend(Rectangle(x_pts=30,
                          y_pts=390,
                          width_pts=170,
                          height_pts=185,
                          line_width_pts=2))
    page.extend(Circle(x_pts=40,
                       y_pts=150,
                       radius_pts=72,
                       line_width_pts=1))
    return page

if __name__ == '__main__':
    page = sample_page()
    print page.render()
