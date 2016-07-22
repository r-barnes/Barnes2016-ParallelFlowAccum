#!/usr/bin/env python3

with open('srtm_names','r') as fin:
  names = fin.readlines()

names = [x.strip() for x in names]
names = set([x.replace('./','').replace('.hgt','') for x in names])

def DoRegion(out,names):
  names     = names.copy()

  all_northings = ["N{0:02}".format(x) for x in range(59,-1,-1)]+["S{0:02}".format(x) for x in range(1,57)]
  all_eastings = ["W{0:03}".format(x) for x in range(180,0,-1)]+["E{0:03}".format(x) for x in range(0,180)]

  for northing in all_northings:
    for easting in all_eastings:
      if northing+easting in names:
        out.write(northing+easting+".hgt,")
      else:
        out.write(' '*11+',')
    out.write('\n')

with open('srtm_global.layout','w') as fout:
  DoRegion(fout,names)
