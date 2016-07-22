Shuttle Radar Topography Mission (SRTM) Global DEM
==================================================
This is a 30m DEM covering the 80% of Earth's land area.

Stats
-----
 * Cells:       12,967,201  (per tile)
 * Dimensions:  3601 x 3601 (per tile)
 * Tiles:       14297
 * Total cells: 185,392,072,697
 * Orientation: Flip tiles vertically and horizontally

For the resampled global SRTM DEM
---------------------------------
 * Cells:       12,967,201    (per tile)
 * Dimensions:  10803 x 10803 (per tile)
 * Tiles:       14297
 * Total cells: 1,668,528,654,273
 * Orientation: Flip tiles vertically and horizontally


Overview
--------



Acquisition
-----------
Acquire data from 

    http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/

using, e.g., 

    wget -r --no-parent --continue --no-clobber http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/

since `lftp` turns out to be too slow here.

To relocate files from out of the subdirectory they get stored in, use:

    find . -iname "*hgt" | xargs -n 1 -P 20 -I {} mv {} ./

To unpack the files use, e.g.:

    find . -iname "*zip" | xargs -n 1 -P 20 unzip


Web Resources
-------------
 * https://lpdaac.usgs.gov/dataset_discovery/measures/measures_products_table/srtmgl1



Resampling the SRTM DEM
-----------------------
To build a rather large DEM, we resample the SRTM global DEM to 3x its original
resolution as follows.

Resampling the DEM is a little tricky. The processes doing it sometimes crash
and the jobs performing it sometimes run out of time. Use the file

    srtm_resample.job

to perform the resampling. **Read the file first to understand it.**

The job is constructed such that you can restart it if something goes wrong.

However, **if something goes wrong, do the following before restarting the
job**.

The job outputs a log script. Use the following command to figure out what the
last files in progress were:

    grep -ohE "[SN][0-9][0-9][WE][0-9][0-9][0-9].hgt" logfile_from_above | uniq | tail -n 100

You should choose a tail at least as large as the number of processors specified
above and, preferrably, larger to account for different speeds of execution.
Delete all of the files in the tail to eliminate the possibility that one of
them is corrupted.

Then list all files in sorted order using 

    ls --sort=size -hl *.tif | tail -n 100'

The smallest files will be on the bottom.

Check the smallest files with, e.g.,

    gdalinfo -stats N25W168.hgt.tif

Delete any files for which you cannot calculate stats.

If you're super paranoid, check stats on many files.

Then, and only then, should you restart the job.

Once everything is done, verify that you have the same number of `hgt` and `tif`
files:

    find -name "*hgt" | wc
    find -name "*tif" | wc

If not, there's a problem and you've got to figure it out.

Another thing you can do is check that everything which the layout file expects
is there:

    cat srtm_global_resampled.layout | tr "," "\n" | sed '/^\s*$/d' | xargs -n1 ls | grep cannot