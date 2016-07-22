#!/usr/bin/env python

import subprocess
import argparse

JOB_CMD = 'sbatch'

parser = argparse.ArgumentParser(description='Run jobs sequentially')
parser.add_argument('-d', '--depend', help='Depend on this job')
parser.add_argument('jobs', metavar='jobs', type=str, nargs='+', help='Jobs to run')
args = parser.parse_args()

dependency = args.depend if args.depend else None

for job in args.jobs:
  if dependency:
    out = subprocess.check_output([JOB_CMD,'--dependency','afterany:'+dependency,job], stderr=subprocess.STDOUT)
    print(' '.join([JOB_CMD,'--dependency','afterany:'+dependency]))
  else:
    out = subprocess.check_output([JOB_CMD,job], stderr=subprocess.STDOUT)
    print(' '.join([JOB_CMD,job]))
  out        = out.split()
  dependency = out[3]
  print('   Job Id: '.format(dependency))