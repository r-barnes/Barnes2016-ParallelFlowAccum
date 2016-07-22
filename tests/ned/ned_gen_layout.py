#!/usr/bin/env python3

with open('ned_tile_names','r') as fin:
  names = fin.readlines()

names     = [x.strip() for x in names]
northings = set([int(x[6:8 ]) for x in names if x.endswith('img')])
eastings  = set([int(x[9:12]) for x in names if x.endswith('img')])
names     = set([x[5:12] for x in names if x.endswith('img')]) #'./imgn42w073_13.img' -> n42w073

def GenGrid(out,northings,eastings,names):
  for northing in reversed(range(min(northings),max(northings)+1,1)):
    for easting in reversed(range(min(eastings),max(eastings)+1,1)):
      if "n{0:02}w{1:03}".format(northing,easting) in names:
        out.write("./imgn{0:02}w{1:03}_13.img,".format(northing,easting))
      else:
        out.write(' '*19+',')
    out.write('\n')

with open('ned_tiles.layout','w') as fout:
  GenGrid(fout,northings,eastings,names)
