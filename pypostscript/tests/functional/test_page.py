from unittest2 import TestCase

from pypostscript.page import A4PortraitPage


class TestA4PortraitPage(TestCase):

    def test_header(self):
        """
        header() shouldn't raise an exception.

        """
        A4PortraitPage().header()
