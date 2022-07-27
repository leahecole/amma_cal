# Amma CAL
This project exists solely to help me plan a blanket I'm crocheting - the [Amma Cal](https://www.ravelry.com/patterns/library/amma-cal)


I want to draw a representation of my color planning and to make sure the distribution of colors is aesthetically pleasing. 

I am a computer scientist and normally I do things zero-indexed when I'm programming. But, when I'm crocheting, everything is 1-indexed. In this program, sometimes I don't make things zero indexed and sometimes I do. Oh well! Maybe someday I'll clean it up. Or not!

Do you want to know my thought process? Check out [my notes](NOTES.md)

# Usage
1. If you want to use this with a different color palette, update the enum of colors to have the hex values that you want. 
1. If necessary, update the SQUARE_WIDTH constant to be the number of pixels you want your squares to be
1. run `python amma.py`

# Attribution
The code found in [shapes.py](./shapes.py) came from [this tutorial](https://www.futurelearn.com/info/courses/object-oriented-principles/0/steps/31483) and I am importing it in my main [amma.py](./amma.py) file. Fwiw, I would not have chosen this license, but because I am utilizing underlying code with this license and modifying it to fit my needs, CC requires I use this license. 

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# TODO
- [x] start out by making each square only fill with white
- [x] properly annotate the Amma type of each square
- [x] create enums of the colors used
- [x] update SAGA squares to fill with the base color on the inner rectangle
- [x] add functions to compute subsquares with each color
- [x] experiment with color
- [ ] add more logic to protect square 4 of Amma.SAGA

# Would be nice TODO
- [x] programmatically generate positioning
- [x] encode row/column into square object


