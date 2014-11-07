# Summoner's rift map gen
This simple script will scrape riot's promotional website about the new summoner's rift updtate to get all the images and create a merged version.
There are 4 zoom levels, from 6 to 3, with 6 being the most zoomed in(and the most detailed/and big map).
Beware, lvl 6 will create a file > 100MB

#### Usage
crete map with zoom level 3
>python map.py

crete map with the desired zoom level(4 in this example)
>python map.py 4

crete map with the desired zoom level(4 in this example) and resize the image to a base width(500px in this example)
>python map.py 4 500
