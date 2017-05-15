#!/bin/bash -l
#SBATCH -J obdt_ext_array
#SBATCH -o obdt_ext_out_%A_%a.txt
#SBATCH -e obdt_ext_err_%A_%a.txt
#SBATCH -t 24:00:00
#SBATCH --mem-per-cpu=8000
#SBATCH --array=1-2
#SBATCH -n 1
#SBATCH -p serial
python3.6 ~/tp2oct2/py/obdt_csc_extended.py "$SLURM_ARRAY_TASK_ID"