Shuttle Radar Topography Mission (SRTM) Regional DEMs
=====================================================

Stats
-----
 * Cells:       12,967,201  (per tile)
 * Dimensions:  3601 x 3601 (per tile)
 * Tiles:       152 - 169
 * Total cells: 1,971,014,552 - 2,191,456,969
 * Orientation: Flip tiles vertically and horizontally



Acquisition
-----------
Acquire data from
    
    http://dds.cr.usgs.gov/srtm/version2_1/SRTM1/

using, e.g.,

    lftp http://dds.cr.usgs.gov/srtm/version2_1/SRTM1/
    mirror .

To unzip the files use, for example:

    cd dds.cr.usgs.gov/srtm/version2_1/SRTM1/
    find . -iname "*zip" | xargs -n 1 -P 20 unzip