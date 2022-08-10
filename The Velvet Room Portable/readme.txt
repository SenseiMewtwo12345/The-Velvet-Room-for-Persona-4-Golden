Welcome to the Velvet Room!

This is an open-source Python 3.9 application with the goal of making fusing Personas in Persona 4 Golden easy. Feel free to modify it and reupload your modified version to your heart's content. I made the scripts for this while learning tkinter at the exact same time, so the GUI is somewhat barebones, and if anyone wants to make improvements to that in particular, feel free. I made this because I wanted it and it didn't exist, not because I wanted to make money off of it or anything.

I tested this pretty thoroughly, but if you encounter any issues I missed, post an Issue on Github. Tell me exactly what you were trying to do so that I can replicate what you did.

=======================
Installation
=======================

Just download the folder and extract it to wherever you want.

=======================
Features:
=======================

Arcana Double Fusion: See the result of fusing two Arcanas.

Arcana Triple Fusion: See the result of fusing three Arcanas.

Persona Double Fusion: Enter two Persona names and see the result.

Persona Triple Fusion: Enter three Persona names and see the result. 

Note that this assumes that all Personas are at their base levels, or at least the highest current level Persona is still the same. If the result of this is wrong, it's probably because one of the Personas you're fusing with is much higher level than normal. Since I don't want to confuse the user with too many entry fields on the Fusion Search windows and because this is such a special case, I'm going to leave this as-is. If you get an incorrect result but you want the result this calculator gives you, simply level the highest base level Persona until it is the highest current level Persona again.

Full Fusion Search: Show all the possible fusions that can be performed with up to 12 Personas

Restricted Fusion Search: Show all the possible fusions that involve a single Persona with up to 12 others.

Persona Search: Search a Persona by name to see information about it.

Persona Compendium: Display the name, level, and Arcana of every Persona in Persona 4 Golden. Can also display all Special Fusions.

=======================
Bugfixes 
=======================
Fixed a bug where Hitokotonusi was named Hitoko-Nushi. (For the record, the second spelling is the correct one, but it turns out that the English version of the game uses the first spelling.) Also solved an issue where some Persona calculations were incorrect because of a small bug in the level calculator where I forgot to account for how the game rounds a result with a decimal. (8/9/22)
Fixed a bug where Andra was referred to as Andras and removed the dependancy on igor.png (8/2/22)
Fixed a bug where Yamatano-Orochi was referred to as Yamata-no-Orochi (7/31/22)