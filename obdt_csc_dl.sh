#!/bin/bash -l
#SBATCH -J obdt_dl
#SBATCH -o output_dl.txt
#SBATCH -e errors_dl.txt
#SBATCH -t 01:00:00
#SBATCH -p serial
python3.6 ~/tp2oct2/py/obdt_csc_dl.py