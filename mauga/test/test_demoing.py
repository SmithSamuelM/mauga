# -*- coding: utf-8 -*-
"""
Unittests
"""
from __future__ import absolute_import, division, print_function

import sys
import os
import unittest

# Import ioflo libs
from ioflo.aid.sixing import *
from ioflo.base.consoling import getConsole
console = getConsole()

from mauga import demoing

def setUpModule():
    console.reinit(verbosity=console.Wordage.concise)

def tearDownModule():
    pass

class BasicTestCase(unittest.TestCase):
    """
    Test Case
    """

    def setUp(self):
        """

        """
        pass

    def tearDown(self):
        """

        """
        pass

    def testBasic(self):
        """
        Test basic function
        """
        console.terse("{0}\n".format(self.testBasic.__doc__))
        console.reinit(verbosity=console.Wordage.profuse)



        console.reinit(verbosity=console.Wordage.concise)


def runOne(test):
    '''
    Unittest Runner
    '''
    test = BasicTestCase(test)
    suite = unittest.TestSuite([test])
    unittest.TextTestRunner(verbosity=2).run(suite)

def runSome():
    """ Unittest runner """
    tests =  []
    names = [
             'testBasic',
            ]
    tests.extend(map(BasicTestCase, names))
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)

def runAll():
    """ Unittest runner """
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BasicTestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__' and __package__ is None:

    #runAll() #run all unittests

    runSome() #only run some

    #runOne('testBasic')


