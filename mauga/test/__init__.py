"""
test package
"""
from __future__ import absolute_import, division, print_function

import sys
import os

from ioflo.aid.sixing import *
from ioflo import test


from ioflo.base.consoling import getConsole
console = getConsole()
console.reinit(verbosity=console.Wordage.concise)

#top = os.path.dirname(os.path.abspath(sys.modules.get(__name__).__file__))
top = os.path.dirname(os.path.dirname
                      (os.path.abspath
                       (sys.modules.get(__name__).__file__)))


if __name__ == "__main__":
    test.run(top)

