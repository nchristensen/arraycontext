__copyright__ = """
Copyright (C) 2020-1 University of Illinois Board of Trustees
"""

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from pytools.tag import Tag, UniqueTag
import sys
from warnings import warn



# {{{ program metadata

class CommonSubexpressionTag(Tag):
    """A tag that is applicable to arrays indicating that this same array
    may be evaluated multiple times, and that the implementation should
    eliminate those redundant evaluations if possible.
    """


class FirstAxisIsElementsTag(Tag):
    """A tag that is applicable to array outputs indicating that the
    first index corresponds to element indices. This suggests that
    the implementation should set element indices as the outermost
    loop extent.
    """

 # {{{ deprecation handling

try:
    from meshmode.transform_metadata import FirstAxisIsElementsTag \
            as _FirstAxisIsElementsTag
except ImportError:
    # placeholder in case meshmode is too old to have it.
    class _FirstAxisIsElementsTag(Tag):  # type: ignore[no-redef]
        pass


if sys.version_info >= (3, 7):
    def __getattr__(name):
        if name == "FirstAxisIsElementsTag":
            warn(f"'arraycontext.{name}' is deprecated. "
                    f"Use 'meshmode.transform_metadata.{name}' instead. "
                    f"'arraycontext.{name}' will continue to work until 2022.",
                    DeprecationWarning, stacklevel=2)
            return _FirstAxisIsElementsTag
        else:
            raise AttributeError(name)
else:
    FirstAxisIsElementsTag = _FirstAxisIsElementsTag


class ParameterValue(UniqueTag):

    def __init__(self, value):
        self.value = value

class IsDOFArray(Tag):
    pass

class IsOpArray(Tag):
    pass

# }}}


# vim: foldmethod=marker
