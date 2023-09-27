# S.P.A.C.E.
## Supply, Prosper, And Conquer Everything

## This is currently not working yet and is in progress

*After untold years, our seed ship has finally located us a home and ended our cryostasis. This new galaxy is full of possibilities, resources, and dangers.*

***And all of it is yours to conquer***

This is a text based board game that places you at the head of a fledgling colony in a galaxy full of planets with resources that will help you expand further into the galaxy. The goal is to have settlements or cities on every planet in the galaxy in as few turns as possible. This game was inspired by the thought of "What if Catan made you move resources from their sources to the location you are building, rather than putting them in your hand?", followed by failed prototypes that resulted in too much info in too small of physical space. Additionally, it came from trying to play 4X space games and getting fed up with the insanely high learning curve and the sheer amount of information being thrown at you.

## How it works

The galaxy is a 15x15 board with each spot consisting of either a planet, an asteriod field, or simply empty space. The board is entirely random, so it may be possible for a galaxy to be created that is not possible to finish.

### Planets, Resources, and Building
Planets produce any number of the 4 resources: Consumables (C), Metals (M), Fuel (F), and Krystals (K)
These resources can be harvested by activating a settlement or city you have built there. They are all used for building, but often have other uses
** - Consumables (C):** Used to activate cities to harvest resrources
** - Metals (M):** Only used to build new things
** - Fuel (F):** Used to move ships 1 space in a turn
** - Krystals (K):** Used to build more advanced things, and move ships 2 spaces in one turn

### Actions

Ships may only take one action per turn

Ships can hold resources in their cargo. This cargo size is different for each ship. Ships have certain actions. All ships have: 
- Load/Unload: add resources from where they are landed to thier cargo add resources from their cargo to where they are landed
- Move: Spend one fuel from it's cargo to move one space cardinally
- Jump: Spend one krystal from it's cargo to move 2 spaces in the same direction
- Attack: not yet implemented

Structures are built on Planets and stay there permanently. Cities and Ship yards are currently the only structures. Both have a level that defines how many actions it can take in a turn

- Harvest: Cities may use one consumable to harvest resources from the planet, adding to the planets cargo according to the amounts specified in their information
- Build ship: Ship yards may spend resources from the planet to build a ship of your choosing. Currently there are only basic cargo ships, but in later versions a higher ship yard level will bring access to other ships 
 
