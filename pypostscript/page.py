# coding=UTF-8
from __builtin__ import open  # For patching in this module's namespace
from os.path import dirname, join

START_TEXT_TEMPLATE = """\
%!PS−Adobe−2.0
%%BoundingBox: 0 0 {width} {height} %
%%Creator: pypostscript
%%EndComments
"""


MM_TO_INCHES = 0.0393700787

PAGE_SIZES = {
    'A0': (841, 1189),
    'A1': (594, 841),
    'A2': (420, 594),
    'A3': (297, 420),
    'A4': (210, 297),
    'A5': (148, 210),
    'A6': (105, 148),
    'A7': (74, 105),
    'A8': (52, 74),
    'A9': (37, 52),
    'A10': (26, 37),
    'B0': (1000, 1414),
    'B1': (707, 1000),
    'B2': (500, 707),
    'B3': (353, 500),
    'B4': (250, 353),
    'B5': (176, 250),
    'B6': (125, 176),
    'B7': (88, 125),
    'B8': (62, 88),
    'B9': (44, 62),
    'B10': (31, 44),
}


class Page(object):
    """
    A single page of PostScript output.

    """

    PAGE_END_PART = 'page_end'
    PARTS_DIR = 'parts_dir'

    @staticmethod
    def from_dimensions(width, height):
        """
        Return a Page sub-class with the given width and height (in mm).

        """
        class NewPage(Page):
            pass
        _mm_to_dots = lambda x: round(x * MM_TO_INCHES * 72, 2)
        width_dots = _mm_to_dots(width)
        height_dots = _mm_to_dots(height)
        NewPage.PAGE_START_TEXT = START_TEXT_TEMPLATE.format(
                                                        width=width_dots,
                                                        height=height_dots)
        return NewPage

    @property
    def PAGE_START_TEXT(self):
        raise NotImplementedError("Page should not be instantiated directly.")

    def extend(self, *ps_objects):
        """
        Add the given ps_object(s) to the Page contents.

        """
        self.__dict__.setdefault('_ps_objects', list()).extend(ps_objects)

    def header(self):
        """
        Return header portion of Page, including any required parts.

        """
        required_parts = set()  # In all cases
        if hasattr(self, '_ps_objects'):
            for ps_object in self._ps_objects:
                if hasattr(ps_object, 'required_parts'):
                    required_parts.update(ps_object.required_parts)

        return '\n'.join([self.PAGE_START_TEXT] +
                         [self.read_part(name=part)
                            for part in required_parts]) + '\n'

    def body(self):
        """
        PostScript string representation of this Page's objects.

        """
        return '\n'.join([ps_object.ps for ps_object in self._ps_objects])

    def footer(self):
        """
        Footer portion of page.

        """
        return self.read_part(name=self.PAGE_END_PART)

    def render(self):
        """
        Provide full output suitable for printer / PS client to open.

        """
        return self.header() + self.body() + self.footer()

    def read_part(self, name):
        """
        Read in boilerplate page part.

        """
        if not hasattr(self, '_root_package_dir'):
            self._root_package_dir = dirname(__file__)

        part_file = open(join(self._root_package_dir, self.PARTS_DIR, name),
                         'r')
        part = part_file.read()
        part_file.close()
        return part


for page_size in PAGE_SIZES:
    width, height = PAGE_SIZES[page_size]
    portrait_name = '{0}PortraitPage'.format(page_size)
    landscape_name = '{0}LandscapePage'.format(page_size)
    locals()[portrait_name] = Page.from_dimensions(width, height)
    locals()[landscape_name] = Page.from_dimensions(height, width)
