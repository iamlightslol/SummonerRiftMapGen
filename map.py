import urllib
from PIL import Image
import sys

url = 'http://promo.na.leagueoflegends.com/sru-map-assets/%s/%i/%i.png'

levels={'6':[48,37],'5':[24,20],'4':[12,10],'3':[6,5]}
zoom_level = '3'

cols = levels[zoom_level][0]
rows = levels[zoom_level][1]
tile_size = 256
resize = 0

def download_map():
	for x in range(0,cols):
		print 'Column %i of %i' % (x + 1, cols),
		for y in range(0,rows):
			print '-',
			img_file = "map/%i-%i.png" % (x,y)
			img_url = url % (zoom_level,x,y)
			urllib.urlretrieve(img_url, img_file)
		print ''

def merge_map():
	full_h = tile_size * (rows-1)
	full = Image.new("RGB", (cols * tile_size, rows * tile_size), "white")
	for x in range(0,cols):
		print 'Column %i of %i' % (x + 1, cols),
		for y in range(0,rows):
			print '-',
			tile = Image.open("map/%i-%i.png" % (x,y))
			full.paste(tile,(x * tile_size,full_h - y * tile_size))
		print ''
	if resize > 0:
		wpercent = (resize/float(full.size[0]))
		hsize = int((float(full.size[1])*float(wpercent)))
		print 'Resizing to %ix%i' % (resize, hsize)
		full = full.resize((resize,hsize), Image.ANTIALIAS)
	print 'Saving'
	full.save("full.png")

if __name__ == '__main__':
	if len(sys.argv) > 1:
		zoom_level = sys.argv[1]
	if len(sys.argv) > 2:
		resize = int(sys.argv[2])
		
	cols = levels[zoom_level][0]
	rows = levels[zoom_level][1]

	print "Downloading map at zoom level %s" % zoom_level
	download_map()
	print "Merging"
	merge_map()
	print "Done"



