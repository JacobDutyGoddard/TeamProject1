# Number Guessing Game
Jacob Duty, Aizen Cannon (The GOAT)

## Number Guessing Game Description
This program is a number guessing game, our first team project ever where Aizen demonstrates AWESOMENESS

### Number Guessing Game Flow Chart
```Game
graph TD;
  main()-->display_menu();
  main()-->gatherPlayers();
  main()-->setRangeOfNumbers();
  main()-->game();
```

#### Function Diagrams

| `main()`    |               |  Jacob Duty  |
| ------------------ | ------------- | ------------ |
| `argument:none`    | takes no input  |              |
| `none`     | runs display_menu() |
| `none`      | returns nothing |
***
| `display_menu()`    |               |     Jacob Duty,  Aizen Cannon   |
| ------------------ | ------------- | ------------ |
| `argument:none`    | takes no arguments |
| `none`     | prints out every option for the game | runs the function relevant to the choice |
| `none`      | handles where to go to next | returns nothing |
***
| `gather_players()`    |               |   Aizen Cannon   |
| ------------------ | ------------- | ------------ |
| `argument:none`    | takes no arguments |
| `string:game_player1`     | prompts the user for 2 inputs | sets the value game_player1 and game_player2 |
| `string:game_player2`      | returns nothing | |
***
| `setRangeOfNumbers()`    |               |    Aizen Cannon   |
| ------------------ | ------------- | ------------ |
| `argument:none`    | takes no arguments |
| `integer:game_minimum`     | prints out every option for the game | runs the function relevant to the choice |
| `integer:game_maximum`      | handles where to go to next | returns nothing |
***
| `game()`    |               |    Jacob Duty, Aizen Cannon   |
| ------------------ | ------------- | ------------ |
| `argument:string:player1, string:player2, integer:min, integer:max`    | takes 4 arguments |
| `integer:correct_num`     | decides a number | runs a loop until the player gets it right |
| `integer:guess`      | swaps back and forth between players | returns winner |
***