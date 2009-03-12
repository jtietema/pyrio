README
===========================================

1. Welcome
2. Requirements / installing
3. Building your own level pak
4. Credits

1. WELCOME
===========================================
Thanks for downloading Pyrio. Pyrio is a Mario clone written in python. It uses graphics
from Secret Maryo Chronicles (http://www.secretmaryo.org/).
This project was intended to be a prototype but it turned out to be quite playable. At the
moment there are only three levels, but creating your own level pak is easy as cake.

If you find any bugs or have suggestions for the project, please report them at our 
issue tracker at the project website (http://bitbucket.org/jtietema/pyrio/).

2. REQUIREMENTS / INSTALLING
===========================================
If you downloaded the Windows installer or the Mac then there is nothing to worry about.
The game should work out of the box.

For people using the source download, the game has the following requirements:
 - Python 2.5
 - Pygame 1.8
 - Psyco (optional) for a decent speed improvement

The game can be started by running: "python main.py" from the root directory of the game.

3. BUILDING YOUR OWN LEVEL PAK
===========================================
If you like the game, but got bored from the three levels that come with the game, then
you must know it is extremely easy to create your own level pak.

Levels are grouped in paks. You can choose the level pak you want to play after selecting
start game in the main menu. A level pak is nothing more than a directory with some levels
in it and pkg.cfg and maps.list files. The levels themselves are ASCII art. So to summarize, creating
your own level requires the following steps:
 - create your own pak directory
 - create some nice ASCII art levels
 - create a pkg.cfg file (associates map files with map names and sets music for map)
 - create a maps.list file (specifies the order in which maps should be played)

Here is a simple listing of characters used in the ASCII art levels:
 # ground (solid dirt)
 - grass with ground underneath
 < vertical ground
 > vertical ground
 / grass corner on top of vertical ground
 \ grass corner on top of vertical ground
 
 ! pipe
 + pipe top
 & brick
 
 * coin
 1 enemy (dragon)
 2 enemy (turtle)
 
 @ end of level door (need to be four in a square)
 0 player start location

Have a look at the default level pak it explains itself quite well.


4. CREDITS
===========================================
Coding:
    Maik Gosenshuis
    Jeroen Tietema

Graphics and Sounds/Music:
    Secret Maryo Chronicles (http://www.secretmaryo.org/)