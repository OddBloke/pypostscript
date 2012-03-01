# coding=UTF-8
from __builtin__ import open  # For patching in this module's namespace
from os.path import dirname, join

A4_PORTRAIT_START = """\
%!PS−Adobe−2.0
%%BoundingBox: 0 0 595.28 841.89 % A4 %
%%Creator: pypostscript
%%EndComments
"""


class Page(object):
    """
    A single page of PostScript output.

    """

    PAGE_END_PART = 'page_end'
    PARTS_DIR = 'parts_dir'

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


class A4PortraitPage(Page):

    PAGE_START_PART = 'page_start_a4portrait'
