# War-of-dots
DISCLAIMER: All credit goes to the original War of dots (https://warofdots.net/). This is a simple barebones war simulation built in python with pygame.

DESCRIPTION:
============

Terrain:
--------
Water: light blue, speed debuf and attack debuff better vision
Plains: green
Forest: dark green, speed debuf and attack debuff worst vision
hills: light grey, speed debuff and attack buff, buffs vision of troop when on
mountains: dark grey, can't be traversed

Cities:
-------
have a position
have a timer that is incrmented each frame
have an owner (player)
have a path that troops produced there are given

timer is constantly evaluated and when is lower than `x` city produces a troop under owner and gives it the cities path
x is lower the less troops/city

flag is drawn on owned cities in color of owner

applys vision and border influence

Troops:
-------
have health, a path, a position and an owner

heal based on distance to nearest city and based on enemy border obstruction

if path, move towards first item (target) any colisions corected fully with troops of the same owner then if the result if valid (not on mountain and not less than x distance of player) commit
if no path to follow slowly correct collisions with other troops + 1 unit

attack nearest enemy

applys vision and border influence

Vision:
-------
flags, cities and terrain can be seen no matter what
troops and the players border are not drawn under vision

influenced by troops and owned cities

Border:
-------
mainly visual, if player has territory between enemy troops and city (e.g. encircled) the enemy troops get a healing debuff

influenced by troops and owned cities

Players:
--------
have starting position, color, troops, and vision and border grids

troops and cities paths are controlled by client

Controls:
---------
Inputs:
Mouse Left-Click (Hold),     Select/Draw,   Selects a player-owned troop (best) or city (best_city) and initiates path drawing.
Mouse Right-Click (Hold),    Pan,           Activates camera movement; offsets camx and camy based on mouse displacement.
Mouse Wheel Up / Button 4,   Zoom In,       Increments zoom_idx and scales the viewport toward the cursor position.
Mouse Wheel Down / Button 5, Zoom Out,      Decrements zoom_idx and scales the viewport away from the cursor position.
Space Bar,                   Confirm Path,  Commits current paths and city_paths to player_input for server transmission and clears local path buffers.
Key: C,                      Clear Paths,   Flushes all pending paths and city_paths without submitting them to the server.
Key: P,                      Toggle Pause,  Toggles the pause state; interrupts event processing and signals the server to pause/unpause.

Strategy:
---------



