from pyformprint.barcode import Code39Barcode, Code93Barcode
from pyformprint.page import Page


def barcode_page():
    page = Page()
    page.extend(Code39Barcode(x_pts=50, y_pts=500, chars='ABC123'))
    page.extend(Code93Barcode(x_pts=50, y_pts=400, chars='ABC987'))
    return page

if __name__ == '__main__':
    page = barcode_page()
    print page.render()
