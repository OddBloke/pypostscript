class Page(object):
    """
    A single page of PostScript output.

    """
    def append(self, ps_object):
        """
        Add the given ps_object to the Page contents.

        """
        self.__dict__.setdefault('_ps_objects', list()).append(ps_object)

    @property
    def ps(self):
        """
        PostScript string representation of this Page object.

        """
        return '\n'.join([ps_object.ps for ps_object in self._ps_objects])
