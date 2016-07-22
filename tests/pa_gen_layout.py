#!/usr/bin/env python3

with open('pa_tile_names','r') as fin:
  names = fin.readlines()

pan_northings = set([int(x[2:6 ]) for x in names if 'PAN' in x])
pan_eastings  = set([int(x[6:10]) for x in names if 'PAN' in x])
pan_names     = set([x[2:10] for x in names if 'PAN' in x]) #'./30001440PAN_dem.tif\n' -> 30001440

pas_northings = set([int(x[2:6 ]) for x in names if 'PAS' in x])
pas_eastings  = set([int(x[6:10]) for x in names if 'PAS' in x])
pas_names     = set([x[2:10] for x in names if 'PAS' in x]) #'./30001440PAS_dem.tif\n' -> 30001440

def GenGrid(out,northings,eastings,names,suffix):
  for northing in range(min(northings),max(northings)+1,100):
    for easting in range(min(eastings),max(eastings)+1,10):
      if str(northing)+str(easting) in names:
        out.write("./{0}{1}{2}_dem.tif,".format(northing,easting,suffix))
      else:
        out.write('                     ,')
    out.write('\n')


with open('pan_tiles.layout','w') as fout:
  GenGrid(fout,pan_northings,pan_eastings,pan_names,'PAN')
with open('pas_tiles.layout','w') as fout:
  GenGrid(fout,pas_northings,pas_eastings,pas_names,'PAS')