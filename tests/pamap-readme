Pennsylvania PAMAP DEM
======================
This is a 1m DEM covering the entire state of Pennsylvania.

Stats
-----
 * Cells:       9,765,625   (per tile)
 * Dimensions:  3125 x 3125 (per tile)
 * Tiles:       6666 (North), 6723 (South)
 * Total cells: 65,097,656,250 (North), 65,654,296,875 (South)
 * Orientation: Flip tiles vertically



Overview
--------
The lidar-derived data products were clipped to the PAMAP tiles and are
organized into datasets by collection year. The resulting digital data files
have names that start with a concatenation of the first four digits of the State
Plane northing and easting that defines the northwest corner of the tile covered
by the data. This number is followed by the state identifier “PA” and the State
Plane zone “N” or “S.” The counties flown each year and the associated State
Plane zones are illustrated on the map below. There is about one tile of overlap
between the two zones.

**NOTE:** Because PAMAP North and South tiles are in different projections they
should not be mixed together!



Acquisition
-----------
To acquire this DEM, run:

    lftp pamap.pasda.psu.edu
    get PAMAP_Tile_IndexNorth.zip PAMAP_Tile_IndexSouth.zip
    mirror -c -P 4 pamap_lidar/cycle1/DEM



Web Resources
-------------
 * http://www.dcnr.state.pa.us/topogeo/pamap/
 * http://www.dcnr.state.pa.us/topogeo/pamap/lidar/index.htm