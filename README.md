Barnes2016-ParallelFlowAccum
============================

**Title of Manuscript**:
Parallel Non-divergent Flow Accumulation For Trillion Cell Digital Elevation Models On Desktops Or Clusters

**Authors**: Richard Barnes

**Corresponding Author**: Richard Barnes (richard.barnes@berkeley.edu)

**DOI Number of Manuscript**
TODO

**Code Repositories**
 * [Author's GitHub Repository](https://github.com/r-barnes/Barnes2016-ParallelFlowAccum)
 * [Journal's GitHub Repository](TODO)

This repository contains a reference implementation of the algorithms presented
in the manuscript above, along with information on acquiring the various
datasets used, and code to perform correctness tests.




Abstract
--------

Continent-scale datasets challenge hydrological algorithms for processing
digital elevation models. Flow accumulation is an important input for many such
algorithms; here, I parallelize its calculation. The new algorithm works on one
or many cores, or multiple machines, and can take advantage of large memories or
cope with small ones. Unlike previous algorithms, the new algorithm guarantees a
fixed number of memory access and communication events per raster cell. In
testing, the new algorithm ran faster and used fewer resources than previous
algorithms exhibiting ∼30% strong and weak scaling efficiencies up to 48 cores
and linear scaling across datasets ranging over three orders of magnitude. The
largest dataset tested has two trillion (2 · 10^12) cells. With 48 cores,
processing required 24 minutes wall-time (14.5 compute-hours). This test is
three orders of magnitude larger than any previously performed in the
literature. Complete, well-commented source code and correctness tests are
available for download from Github.





Compilation
-----------

The program can be produced simply by running **make**. However, certain
prerequisites are necessary for this to be successful.

For **compilation**, the following command will set you up on a Debian-based
system:

    sudo apt-get install make openmpi-bin libgdal-dev libopenmpi-dev

If you wish (as I did) to compile the code on XSEDE, certain modules must be
loaded:

    module load intel/2015.2.164
    module load mvapich2_ib

Note that temporary files can be stored in:

    /oasis/scratch/comet/$USER/temp_project

or some similar directory.

Running `make` will produce an executable called `parallel_d8_accum.exe`.

Running the above compiles the program to run the _cache_ strategy. Using `make
compile_with_compression` will enable the _cacheC_ strategy instead. This
strategy is not compiled by default because it requires the Boost Iostreams
library. This libary can be installed with:

    sudo apt-get install libboost-iostreams-dev



Running the Program
-------------------

`parallel_d8_accum.exe` can be run without arguments from the command line to
show a comprehensive explanation of the program and its options. This same text
is in the file `help.txt`.

In order to process data, you will need to run `parallel_d8_accum.exe` in MPI.
For example:

    mpirun -n 4 ./parallel_d8_accum.exe one @offloadall dem.tif outroot -w 500 -h 500

In the foregoing example `-n 4` indicates that the program should be run in
parallel over four processes. One of these processes (the one with MPI rank #0)
acts as a master process. It does limited computation but stores information
from all of the other processes. This requires less memory than one would think,
as discussed in the manuscript.



Layout Files
------------

A layout file is a text file with the format:

    file1.tif, file2.tif, file3.tif,
    file4.tif, file5.tif, file6.tif, file7.tif
             , file8.tif,          ,

where each of fileX.tif is a tile of the larger DEM collectively described by
all of the files. All of fileX.tif must have the same shape; the layout file
specifies how fileX.tif are arranged in relation to each other in space. Blanks
between commas indicate that there is no tile there: the algorithm will treat
such gaps as places to route flow towards (as if they are oceans). Note that the
files need not have TIF format: they can be of any type which GDAL can read.
Paths to fileX.tif are taken to be relative to the layout file.

Several example layout files are included in the `tests/` directory and end with
the `.layout` extension.



MPI Profiling
-------------
Although the program tracks its total communication load internally, I have also
used [mpiP](http://mpip.sourceforge.net/) to profile the code's communication.
The code can be downloaded [here](http://mpip.sourceforge.net/) and compiled
with:

    ./configure --with-binutils-dir=/usr/lib
    make shared
    make install #Installs to a subdirectory of mpiP

Prerequisites include: `binutils-dev`.

mpiP can be used to profile _any_ MPI program without the need to compile it
with the program. To do so, run the following line immediately before launching
`mpirun`:

    export LD_PRELOAD=path/to/libmpiP.so

Although the program tracks its maximum memory requirements internally, I have
also used `/usr/bin/time` to record this. An example of such an invocation is:

    mpirun -output-filename timing -n 4 /usr/bin/time -v ./parallel_d8_accum.exe one @offloadall dem.tif outroot -w 500 -h 500

This will store memory and timing information in files beginning with the stem
`timing`.



Testing
-------

For **running tests**, the following command will set you up on a Debian-based
system:

    sudo apt-get install python3-gdal python-gdal gdal-bin

The directory `tests` contains all of the information and layouts associated
with the tests described in the paper. The most immediately useful are probably
the `tests/beauford` test, which includes a small DEM suitable for testing the
correctness of various tile sizing configurations, and the `tests/srtm_small`
test (see the `README.md` file in that directory for further information), which
tests the "many" mode on a 3x3 excerpt of the SRTM Region 3 data.

Other subdirectories of `tests` are named for the dataset they pertain to and
contain directions for acquiring the datasets and example jobs for running them
using SLURM.

The `beauford` and `srtm_small` tests can be run using the `test.py` script.
This script can be running using one of the following: 

    ./test.py tests/beauford/beauford.tif
    ./test.py tests/srtm_small/srtm_small.layout

Once data has been acquired and placed in these directories.

In the case of a layout file being used, the `test.py` script will merge all of
the tiles together. This merged file, or, in the case of a single input file
being used, that file, will be depression filled using the algorithm in a
single-core mode. This generates an authoritative answer against which
correctness is checked. The program then iterates over many tile sizes to ensure
that they all compare correctly against this authoritative answer.



Notes
-----

The `communication.hpp` header file abstracts all of the MPI commands out of
`main.cpp`. This is useful for generating communication statistics, but also
preempts a day when the message passing is reimplemented using `std::threads` so
that the program can be compiled for use on a single node/desktop without having
to include MPI as a dependency.


RichDEM
-------

This code is part of the RichDEM codebase, which includes state of the art
algorithms for quickly performing hydrologic calculations on raster digital
elevation models. The full codebase is available at
[https://github.com/r-barnes](https://github.com/r-barnes)
