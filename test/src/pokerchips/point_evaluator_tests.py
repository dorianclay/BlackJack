import unittest

from library.chip import Chip
from library.chip import Color
from src.pokerchips.point_evaluator import evaluate_points

class PointEvaluatorTestCase(unittest.TestCase):

  def test_with_single_white(self):
    chips = [Chip(Color.WHITE)]
    points = evaluate_points(chips)
    self.assertEqual(1, points)

  def test_all_colors(self):
    for color in Color:
      chips = [Chip(Color.color)]
      points = evaluate_points(chips)
      self.assertEqual('''proper value''', points)
      

  
if __name__ == '__main__':
  unittest.main()