class Page(object):
    """
    A single page of PostScript output.

    """
    def extend(self, *ps_objects):
        """
        Add the given ps_object(s) to the Page contents.

        """
        self.__dict__.setdefault('_ps_objects', list()).extend(ps_objects)

    @property
    def ps(self):
        """
        PostScript string representation of this Page object.

        """
        return '\n'.join([ps_object.ps for ps_object in self._ps_objects])
