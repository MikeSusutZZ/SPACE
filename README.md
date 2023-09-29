# S.P.A.C.E.
## Supply, Prosper, And Conquer Everything

## This is currently not working yet and is in progress

*After untold years, our seed ship has finally located us a home and ended our cryostasis. This new galaxy is full of possibilities, resources, and dangers.*

***And all of it is yours to conquer***

This is a text based board game that places you at the head of a fledgling colony in a galaxy full of planets with resources that will help you expand further into the galaxy. *The goal is to have cities on every planet in the galaxy in as few turns as possible.* This game was inspired by the thought of "What if Catan made you move resources from their sources to the location you are building, rather than putting them in your hand?", followed by failed prototypes that resulted in too much info in too small of physical space. Additionally, it came from trying to play 4X space games and getting fed up with the insanely high learning curve and the sheer amount of information being thrown at you.

## How it works

The galaxy is a grid with each spot consisting of either a planet, an asteriod field, or simply empty space. The board is entirely random, so it may be possible for a galaxy to be created that is not possible to finish.

### Planets, Resources, and Building
Planets produce any number of the 4 resources: Consumables (C), Metals (M), Fuel (F), and Krystals (K)
These resources can be harvested by activating a settlement or city you have built there. They are all used for building, but often have other uses
** - Consumables (C):** Used to activate cities to harvest resrources
** - Metals (M):** Only used to build new things
** - Fuel (F):** Used to move ships 1 space in a turn
** - Krystals (K):** Used to build more advanced things, and move ships 2 spaces in one turn

### The Galactic Map
The map will show every location in the galaxy. Each location has 2 values, Whether it is a:
- 'P' Planet
- 'A' Asteroid Field
- '_' Empty Space
The second value is what is available to be activated on the planet (regardless of if you have the resources to do so). They appear in this priority, overwriting the others below it: 
- '*' Available to harvest
- '`' Able to build ships
- '^' Ship available to be used

### Locations
- Planets: Where structures can be built and resources stored
- Asteroids: If a ship ends a turn here, there is a 50% chancce of it being **destroyed**!
- Empty space: Nothing of note, just for you to fly through

### Actions

#### Ships
Ships may only take one action per turn

Ships can hold resources in their cargo. This cargo size is different for each ship. Ships have certain actions. All ships have: 
- Load/Unload: add resources from where they are landed to thier cargo add resources from their cargo to where they are landed
- Move: Spend one fuel from it's cargo to move one space cardinally
- Jump: Spend one krystal from it's cargo to move 2 spaces in the same direction
- Attack: not yet implemented

Structures are built on Planets and stay there permanently. Cities and Ship yards are currently the only structures. Both have a level that defines how many actions it can take in a turn

- Harvest: Cities may use one consumable to harvest resources from the planet, adding to the planets cargo according to the amounts specified in their information
- Build ship: Ship yards may spend resources from the planet to build a ship of your choosing. Currently there are only basic cargo ships, but in later versions a higher ship yard level will bring access to other ships 
 
### Getting Started
Just loaded up your first game and not sure where to start?
- When asked for a seed, enter 2
- When asked for a galactic size, enter 4
The screen should hopefully look like this:
```
Do you want to use a seed? (either n or enter seed): 2
What size galaxy would you like?(rec. 5 for new players): 4
      ( A ) ( B ) ( C ) ( D ) 

( 1 ) [_,_] [A,_] [_,_] [_,_] 

( 2 ) [A,_] [_,_] [P,_] [P,_] 

( 3 ) [A,_] [A,_] [P,*] [_,_] 

( 4 ) [_,_] [P,_] [_,_] [A,_] 
```

This map is nice and forgiving for new players, only 3 more planets to reach for and no asteroids in the way.

Firstly, harvest resources from your homeworld on C 3. You already start with a ship yard and a city with a single consumable to activate it. *Your homeworld will always start this way, always have the same stats, and always be in the center(ish) of the map*. With these new metals you've gathered, build a cargo ship. That's the end of turn one! End the turn by entering 'e' on the map. Very simple to start, but gets more exciting once you have more going on. 

Next check out the galactic map by entering 'i' on the map. This will print out all information of every location in the galaxy (you may have to scroll up). Pick a planet near by to target next. In this case, C 2 is closest and has a good set of resources, so that will be the next planet we want to build a city on. After another harvest you'll have 3C, 4F, and 2M on the planet, just one metal short of the building requirement for a city. End the round again so we can harvest enough on the next turn.

After another harvest, you're ready to begin loading your ship. Choose the Use ships option, pick your cargo ship and load it with 3M and 2C to build a new city, and 1F to fly the ship. The loading process is described through entering 'h' for help. This loading process uses the ship for the turn, so you'll need to wait until next turn to move it.

Harvest again, build another ship and load it up with fuel to fly and at least one Comsumable, preping it to supply the new city you'll be building, and fly your already loaded cargo ship up to C 2. This also 'uses' the ship, so you'll unload it and build your city next turn.

Your loaded cargo ship ship is now at C 2 and ready to unload. Drop all of the resources on board, and build a city! Unfortunately, you don't have any Consumables to activate your new city, but that's what your second ship is for. Move that ship loaded with consumables up to C 2. Don't forget to harvest on your home world too!

On your next turn you're ready to activate C 2! Since it produces 1C, it's self sustaining, but you'll need to supply your further cities from your homeworld. It also produces Krystal, which is needed to upgrade your cities, which could help you develop faster by allowing multiple activations of a single planet. 

From there you're well set up to continue on to the other 2 planets in this small galaxy!