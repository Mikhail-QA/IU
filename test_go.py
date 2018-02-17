import unittest
from Smoke.test_21 import PlayVideoYouTube
from Smoke.test_20 import PlayVideoIu


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(PlayVideoIu))
suite.addTest(unittest.makeSuite(PlayVideoYouTube))
