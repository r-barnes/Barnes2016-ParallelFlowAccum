if [ "$gCORES" -ge $((24*(SLURM_JOB_NUM_NODES-1))) ] && [ "$gCORES" -le $((24*SLURM_JOB_NUM_NODES)) ]; then
  module load boost/1.55.0
  module load intel/2015.2.164
  module load mvapich2_ib

  gLAYOUT=/oasis/scratch/comet/rbarnes1/temp_project/gisdata/$gDATASET/$gLAYER/$gLAYOUTNAME
  gOUTPUTDIR=/oasis/scratch/comet/rbarnes1/temp_project/gisdata/$gDATASET/$gOUTLAYER

  rm -rf   $gTEMPDIR
  mkdir -p $gTEMPDIR
  rm -rf   $gOUTPUTDIR
  mkdir -p $gOUTPUTDIR

  if [[ ${gEVICT:0:1} != "@" ]] ; then 
    gEVICT=$gEVICT/temp-%f.tif
  fi

  $gMPI -n $gCORES $gEXE $gONEMANY $gEVICT $gLAYOUT $gOUTPUTDIR/%f.tif
else
  echo "Insufficient cores available on $SLURM_JOB_NUM_NODES nodes!"
fi