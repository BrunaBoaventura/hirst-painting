# Hirst Painting

This project creates a "Dot painting" in the same style as the artist Damien Hirst in an automated way.

## History

Damien Hirst is one of the most successful and controversial artists and has been dominating the British art 
scene since the 1990s. Though he became famous through a series of artworks centered on the death motif, 
the Spot Oaintings have become his signature. His spots are easily recognizable and widely sought after by 
art collectors.
[Source](https://publicdelivery.org/damien-hirst-spot-paintings/)

## Process

### Color Matching

For the color matching, the `colorgram` [module](https://pypi.org/project/colorgram.py/) was used which extracts colors 
out of a picture. I have selected one result out of Google which contained colors I wished to use in my project.

<img src="file://./image.jpg" alt="alt text" width="300"/>

### Using the colors

After the color matching, I obtained the RGB values of the image and used those in my final program.

### Turtle

The `turtle` [module](https://docs.python.org/3/library/turtle.html#turtle.setheading) was used to build the image.