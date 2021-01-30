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

## Why Object Oriented Programming

We have classes, which are a blueprint for an object. This abstracts away the implementation of the object.

OOP provides abstraction so that we know how a class is used, but don't have to know how it works.

Some of these basics exist in C as well, such as with `struct` and header files.

Above all, OOP provides *polymorphism*. This allows us to refer to an object as if it were a different kind of object, as long as they're in the same inheritance tree. This allows us to write code that acts as a "plugin," where the client can implement their own version of a class with its own behaviors.

Polymorphism is extremely important and helpful. For instance, if we use mySQL for a database, then want to switch from MongoDB, it's easy to switch if there's a "middleman" access layer.

## SOLID Principles

### **S:** Single Responsibility Principle

The Single Responsibility Principle (SRP) states that any class must have one, and only one, reason to change. If a class has more than one reason to change, it should be refactored (larger, structural editing).

The motivation is to minimize changes we will have to make, when inevitably requirements change.

### **O:** Open-Closed Principle

Open for extension, closed for modification.

E.g. what if someone wanted to create a hearts game using the code we used for our blackjack game? 

If they can increase complexity or add features, then we've succeeded in being "open for extension."

If they don't have to modify any of our code to make their game, then we've succeeded in being "closed for modification."

### **L:** Liskov Substitution Principle

If you have a superclass, then anytime you create a subclass, you should be able to use that subclass anywhere the superclass is used.

If you're going to use a substitution, any methods it uses from the parent class shouldn't have suprising side effects or behavior that the person wouldn't expect.

Example: the rubber duck class. If we create a robot duck class, then we need to add a "replace battery" function. If we have a list of rubber ducks, we can't just give a list of robot ducks, because it won't know about those extra requirements.

If we have to create a robot duck, don't subclass duck. A separate class should be made, probably as a composition of the duck and additional logic around the battery.

E.g. we have a data access layer, we shouldn't do something or have properties that require special attention.

### **I:**

### **D:** Dependency Inversion Principle



### Refuse Bequest Antipattern

Whenever there are subclasses, must think about whether they'll make use of what the parent class has. If parent classes have too many methods, then the subclasses basically just implement empty versions.

One way to get around this is to design with **composition over inheritance**. This means rather than inheriting from a class, create a class that is a composition of multiple classes. This prevents getting locked into a heirarchy.

Classic example: if you want to list a bunch of things, and want some properties surrounding it, don't create a subclass of an array. Instead, you create a class that has an array and also the other properties that you want.

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

## Dealer Class

- Abstract/virtual class: intended that a subclass is instatiated.
- Initially deals cards to all players.
- Draw a card for a given player.

### BlackJack Dealer Class

- Deals two cards to each player.
- Draw a card for tne given player.

## Player Class

- Name.
- Hand (cards).

## Game Class (GameObject)

- Abstract class.
- Starts with an array of players and a dealer.
- Play a turn of the game.

## BlackJack Game Class

- Starts with an array of players and a dealer.
- When playing a turn:
  - Force them to take another card!