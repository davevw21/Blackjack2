# Blackjack2
a game of blackjack using the deck of cards API

This is a game of blackjack.
The deck of cards uses an API located at https://deckofcardsapi.com/

A typical game of blackjack uses 6 decks of cards however you may choose how many decks are used.

Typical blackjack game rules apply.  

The object of the game is to get a blackjack, get 21 by drawing cards, or get as close to 21 without exceeding 21.

The initial cards are drawn from the deck in the order player, dealer, player, dealer.
Cards are valued to look for a possible blackjack.

The player is asked if they want to hit (take another card) or stay (stay at the current card count)

The dealer then draws cards if his hand is equal to or less than 17.
The dealer is not allowed to draw if his hand exceeds 17

Cards are then scored

If player gets 21 player wins
if dealer gets 21 dealer wins
if both get 21 its a push

if none of these apply:
a tied hand is a push
highest hand not exceding 21 wins

I did not configure rules for splits.
I also did not configure rules for betting.

I hope to continue to work both of those in with future scripts. 

Enjoy
