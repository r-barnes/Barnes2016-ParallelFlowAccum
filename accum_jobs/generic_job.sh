module load boost/1.55.0
module load intel/2015.2.164
module load mvapich2_ib

gLAYOUT=/oasis/scratch/comet/rbarnes1/temp_project/gisdata/$gDATASET/$gLAYER/$gLAYOUTNAME
gOUTPUTDIR=/oasis/scratch/comet/rbarnes1/temp_project/gisdata/$gDATASET/$gOUTLAYER

rm -rf   $gTEMPDIR
mkdir -p $gTEMPDIR
rm -rf   $gOUTPUTDIR
mkdir -p $gOUTPUTDIR

$gMPI $gMPIOPTS $gEXE $gONEMANY $gEVICT $gLAYOUT $gOUTPUTDIR/%f.tif