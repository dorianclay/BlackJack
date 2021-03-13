import unittest

loader = unittest.TestLoader()
tests = loader.discover('.', '*tests.py')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
