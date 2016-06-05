# practicerl
My first attempt at a Roguelike. This will attempt to create a Roguelike 
following the libtcod tutorial but with the following objectives.
1) Apply OOP and Pythonic thinking from the beginning
2) Implemented using just curses instead of libtcod
3) Test bed for creating a future Roguelikes

I won't be using libtcod to create this roguelike for a few reasons. 
1) It lacks proper 64bit support, which meant I couldn't get it to install on
my Chromebook. In addition, it doesn't seem to compile or install in a
container on CodeAnywhere (though I think I could get it to work there with
time).
2) It will deepen my understanding of what's happening and why if I'm adapting
one tutorial to a different library. Part of the impetus for this is learning
how to write a program that runs continuously rather than like a script.
Merging two different implementations of a program loop (libtcod and curses)
should give me a greater understanding of how they work for other, more
ambitious undertakings.