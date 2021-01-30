from os.path import dirname, realpath
import unittest
import sys

sys.path.append(dirname(realpath(__file__)) + '\..\..')

from library.card import Card
from library.card import Suit
from src.blackjack.point_evaluator import evaluate_points

class PointEvaluatorTestCase(unittest.TestCase):

  def test_with_single_ace(self):
    cards = [Card(1, Suit.DIAMONDS)]
    points = evaluate_points(cards)
    self.assertEqual(11, points)

  def test_with_no_aces(self):
    for value in range(2, 14):
      cards = [Card(value, Suit.DIAMONDS)]
      points = evaluate_points(cards)
      self.assertEqual(value, points)
  
  def test_with_multiple_aces(self):
    cards = [Card(1, Suit.DIAMONDS), Card(1, Suit.DIAMONDS)]
    points = evaluate_points(cards)
    self.assertEqual(12, points)
  
  def test_with_ace_and_bust(self):
    cards = [Card(10, Suit.DIAMONDS), Card(10, Suit.DIAMONDS), Card(1, Suit.DIAMONDS)]
    points = evaluate_points(cards)
    self.assertEqual(21, points)
  
  def test_with_two_aces_and_bust(self):
    cards = [Card(9, Suit.DIAMONDS), Card(1, Suit.DIAMONDS), Card(1, Suit.DIAMONDS)]
    points = evaluate_points(cards)
    self.assertEqual(21, points)


if __name__ == '__main__':
    unittest.main()