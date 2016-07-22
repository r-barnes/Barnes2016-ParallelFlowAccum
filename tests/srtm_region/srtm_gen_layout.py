#!/usr/bin/env python3

with open('srtm_names','r') as fin:
  names = fin.readlines()

names     = [x.strip() for x in names]
names     = [x.replace('.zip','') for x in names]

def DoRegion(out,names,region):
  names     = [x for x in names if region in x]
  northings = set([int(x[13:15]) for x in names])
  eastings  = set([int(x[16:19]) for x in names])
  names     = set([x[12:19] for x in names]) #'./Region_01/N40W124.hgt' -> N40W124

  for northing in reversed(range(min(northings),max(northings)+1,1)):
    for easting in reversed(range(min(eastings),max(eastings)+1,1)):
      if "N{0:02}W{1:03}".format(northing,easting) in names:
        out.write("./{0}/N{1:02}W{2:03}.hgt,".format(region,northing,easting))
      else:
        out.write(' '*23+',')
    out.write('\n')

for region in ["Region_01","Region_02","Region_03","Region_04","Region_05","Region_06","Region_07"]:
  with open('{0}.layout'.format(region),'w') as fout:
    DoRegion(fout,names,region)
