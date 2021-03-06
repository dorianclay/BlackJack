import { Card, Suit } from './card';

export function textFormatForCard(card: Card): string {
  const valueString = textFormatForValue(card.value);
  const suitString = textFormatForSuit(card.suit);
  return `${valueString} of ${suitString}`;
}

function textFormatForValue(value: number): string {
  switch (value) {
    case 1:
      return 'Ace';
    case 11: 
      return 'Jack';
    case 12:
      return 'Queen';
    case 13:
      return 'King';
    default:
      return `${value}`;
  }
}

function textFormatForSuit(suit: Suit): string {
  switch (suit) {
    case Suit.CLUBS:
      return 'Clubs';
    case Suit.DIAMONDS:
      return 'Diamonds';
    case Suit.HEARTS:
      return 'Hearts';
    case Suit.SPADES:
      return 'Spades';
  }
}