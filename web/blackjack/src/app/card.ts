export enum Suit {
  CLUBS = 1,
  DIAMONDS = 2,
  HEARTS = 3,
  SPADES = 4
}

export class Card {
  constructor(public suit: Suit, public value: number) {}
}