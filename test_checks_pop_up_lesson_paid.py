import unittest
from PopUp.test_1_Платный_урок_проверка_через_все_места import CheckAppearancePopUpInAllPlaces

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(CheckAppearancePopUpInAllPlaces))