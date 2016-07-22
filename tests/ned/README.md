National Elevation Dataset (NED) DEM
====================================
This is a 10m DEM covering the entire United States.

Stats (for 10m DEM)
-------------------
 * Cells:       116,899,344     (per tile)
 * Dimensions:  10812 x 10812   (per tile)
 * Tiles:       1023
 * Total cells: 119,588,028,912
 * Orientation: Flip tiles vertically and horizontally



Overview
--------
NED data are available nationally and in Puerto Rico at resolutions of 1
arc-second (about 30 meters) and 1/3 arc-second (about 10 meters), and in
limited areas at 1/9 arc-second (about 3 meters). In most of Alaska, only lower
resolution source data are available. As a result, most NED data for Alaska are
at 2-arc-second (about 60 meters) grid spacing. Part of Alaska is available at
the 1- and 1/3-arc-second resolution.

Data units are in feet, and all data use the NAD83 horizontal datum, GRS80
ellipsoid, NAVD88 vertical datum, and GEOID03 National Geodetic Survey.



Acquisition
-----------
Acquire data from:

    ftp://rockyftp.cr.usgs.gov/vdelivery/Datasets/Staged/Elevation/13/IMG/

After unpacking the NED tiles, grab only the files which begin with `imgn` and
end with `img`.



Web Resources
-------------
 * http://nationalmap.gov/3DEP/3dep_prodmetadata.html