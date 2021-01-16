# BlackJack
A project to practice the SOLID OOP Design Principles.

## Gameplay

1. You are dealt 2 cards.
2. You have the choice to hit or stay.
3. If you hit, you are dealt another card.
4. If your point value is over 21, you bust and lose.
5. If your point value is 21 or less, repeat step 2.
6. If you stay, the dealer hits until they are over 16.
7. Highest point value under 22 wins. Player wins ties.

## SOLID Principles

### S: Single Responsibility Principle

The Single Responsibility Principle (SRP) states that any class must have one, and only one, reason to change. If a class has more than one reason to change, it should be refactored (larger, structural editing).

The motivation is to minimize changes we will have to make, when inevitably requirements change.

### O: Open-Closed Principle

Open for extension, closed for modification.

E.g. what if someone wanted to create a hearts game using the code we used for our blackjack game? 

If they can increase complexity or add features, then we've succeeded in being "open for extension."

If they don't have to modify any of our code to make their game, then we've succeeded in being "closed for modification."

### L:

### I:

### D:

## Card Class

- A number and a suit
- Suits:
  - Clubs
  - Diamonds
  - Hearts
  - Spades

## Deck Class

- Keeps track of cards.
- Maintains suits.
- Maintains number range.
- Could be changed for different card types (e.g. ace high/low).
- Should be able to see contents of deck.
- Should be able to modify contents of deck.
- Each card: number and suit

## Game Deck Class

- Constructed out of several `deck` classes.
- Could change if we want more than one deck.
- Draw cards.

## Blackjack Point Class

- Determines the point value of a given card.
- e.g. aces worth 1 or 11.