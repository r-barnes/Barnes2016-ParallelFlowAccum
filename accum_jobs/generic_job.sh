module load boost/1.55.0
module load intel/2015.2.164
module load mvapich2_ib

rm -rf   /oasis/scratch/comet/rbarnes1/temp_project/temp/$gDATASET
mkdir -p /oasis/scratch/comet/rbarnes1/temp_project/temp/$gDATASET
rm -rf   /oasis/scratch/comet/rbarnes1/temp_project/output/$gDATASET
mkdir -p /oasis/scratch/comet/rbarnes1/temp_project/output/$gDATASET

gLAYOUT=/oasis/scratch/comet/rbarnes1/temp_project/gisdata/$gDATASET/$gLAYER/layout.layout
gOUTPUT=/oasis/scratch/comet/rbarnes1/temp_project/output/$gDATASET/%f.tif

$gMPI $gEXE $gONEMANY $gEVICT $gLAYOUT $gOUTPUT  /oasis/scratch/comet/rbarnes1/temp_project/srtm_region/Region_01/orig/Region_01.layout 