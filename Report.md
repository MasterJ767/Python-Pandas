Reflective Report
=================

Summary
-------

The python code which I have adapted based on the tutorial I was given and then the various tutorials on the
https://www.panda3d.org/manual/ website generates: the standard Panda3d scenery base with a red hue.
Then it renders 16 pandas of varying sizes and colours and sets them up to walk on predefined motions paths.
Using functions I have made it possible to vary the scale, walk speed, turn speed, colour and the starting and ending x,
y and z co-ordinates for all 16 pandas. Pandas 13 - 16 take a square, clock-wise route around the map unlike the other
12 pandas who continue to move in a singular plane. Finally I added a royalty free mp3 file to play in the background,
some idle Panda noises and a large piece of text stating "Pandemonium" to caption this creation and add an additional 
dimension to it.

I initially found it very difficult to get started on this project as I had trouble installing Panda3d and ensuring
that I was using the correct version of Python (version 3.7). Once I got past this setback I found the Panda3d tool was 
relatively straightforward to use. A few errors occurred when I attempted to add my own things to the code such as 
varying the volume of the sound randomly and I could not work out how to add more colours to the project with panda3d 
than red, yellow, green, cyan, blue, magenta, black and white. I also attempted to use one function to call multiple
pandas but I couldn't work out how to change the variable names without copying the function block and changing them
manually. I struggled to utilise any form of iteration inside of functions and I'm not sure whether that was due to my
lack of knowledge of python or the limitations of the coding language.

Past use of tools
-----------------

I am fairly familiar with Python. I was first introduced to it in GCSE Computing and I have continued to use the 
programming software on and off ever since. I didn't do Computer Science as part of the IB so my python skills are a
bit rusty. This was my first experience using pip, venv and Panda3d. Despite the difficulties I had with the initial
install I found each other tools to be very enjoyable to use.

Future development projects
---------------------------

I intend to continue using pip and venv to install other external libraries, as well as the dependencies for these
libraries, as this software streamlines the process and makes it much simpler to use external libraries. I will also 
take some of the uses of functions and variables into future projects such as ``def __init__(self):`` which I would like
to better understand how it works so that I may make more effective and efficient use of functions and variables in the
future.
