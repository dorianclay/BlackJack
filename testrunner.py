import unittest

loader = unittest.TestLoader()
tests = loader.discover('.', '*tests.py')
testRunner = unittest.runner.TextTestRunner()
results = testRunner.run(tests)
if results.wasSuccessful():
    exit(0)
else:
    exit(1)
