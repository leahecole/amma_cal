# Amma CAL
This project exists solely to help me plan a blanket I'm crocheting - the [Amma Cal](https://www.ravelry.com/patterns/library/amma-cal)


I want to draw a representation of my color planning and to make sure the distribution of colors is aesthetically pleasing. 

I am a computer scientist and normally I do things zero-indexed when I'm programming. But, when I'm crocheting, everything is 1-indexed. In this program, sometimes I don't make things zero indexed and sometimes I do. Oh well! Maybe someday I'll clean it up. Or not!

# Usage
1. If you want to use this with a different color palette, update the dictionary of colors to have the hex values that you want. 
1. If necessary, update the SQUARE_WIDTH constant to be the number of pixels you want your squares to be
1. run `python amma.py`



# TODO
- [x] start out by making each square only fill with white
- [x] properly annotate the Amma type of each square
- [x] create enums of the colors used
- [x] update SAGA squares to fill with the base color on the inner rectangle
- [ ] add functions to compute subsquares with each color
- [ ] experiment with color

# Would be nice TODO
- [x] programmatically generate positioning
- [x] encode row/column into square object
