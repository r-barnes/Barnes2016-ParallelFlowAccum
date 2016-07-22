Scaling Tests
=============

Strong scaling tests were performed on the largest square subset of tiles in the
datasets without any gaps. For each dataset this square had dimension NxN where
N was:

    ./pamap/pan_tiles_small.layout              3
    ./srtm_region/nasa_srtm3_small.layout       3
    ./srtm_region/Region_07.layout              3
    ./srtm_region/Region_04.layout              7
    ./srtm_region/Region_06.layout              8
    ./srtm_region/Region_05.layout              9
    ./srtm_region/Region_03.layout              10
    ./srtm_region/Region_01.layout              11
    ./srtm_region/Region_02.layout              11
    ./ned/ned_tiles.layout                      19
    ./srtm_global/srtm_global.layout            39
    ./srtm_global/srtm_global_resampled.layout  39
    ./pamap/pan_tiles.layout                    44
    ./pamap/pas_tiles.layout                    44

Weak scaling tests were performed on increasing numbers of rows of the largest
square subset of tiles. This data can be produced from the largest square tile
using:

    echo {1..38} | tr " " "\n" | xargs -n 1 sh -c 'head -n $0 srtm-39.layout > /z/srtm-$0.layout'

All the necessary layout files are in this directory, but should be copied to
the appropriate data directories before running jobs.