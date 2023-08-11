# Not The Game

## Design

```mermaid
classDiagram
Game *-- Card : 100 cards
Game *-- Deck
Game *-- Hand : 1 hand per player
Game *-- Column : 2 Ascending
Game *-- Column : 2 descending
Card ..o Deck : available
Card ..o Hand : drawn
Card ..o Column : played
Column : Direction
```
