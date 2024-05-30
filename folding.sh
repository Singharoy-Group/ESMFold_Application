#!/bin/bash

#SBATCH -N 1            # number of nodes
#SBATCH -c 32            # number of cores
#SBATCH -t 7-00:00:00   # time in d-hh:mm:ss
#SBATCH -p general      # partition
#SBATCH -q public       # QOS
#SBATCH -G a100:1
#SBATCH -o slurm.%j.out # file to save job's STDOUT (%j = JobId)
#SBATCH -e slurm.%j.err # file to save job's STDERR (%j = JobId)
#SBATCH --mail-type=NONE # Send an e-mail when a job starts, stops, or fails
#SBATCH --export=NONE   # Purge the job-submitting shell environment

module load mamba/latest
source activate ESM

python folding_v2.py list1.txt

conda deactivate
