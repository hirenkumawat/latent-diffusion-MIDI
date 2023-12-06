#!/bin/bash
#SBATCH -Jtrain					# Job name
#SBATCH -N1 --gres=gpu:4 -C V100-32GB   # Number of nodes, GPUs, and cores required
#SBATCH -oReport-%j.out   
#SBATCH --mem-per-cpu=20G                        # Memory per core
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH -t240                                   # Duration of the job (Ex: 15 mins)
#SBATCH --mail-type=BEGIN,END,FAIL              # Mail preferences
#SBATCH --mail-user=hkumawat3@gatech.edu        # E-mail address for notifications
cd $SLURM_SUBMIT_DIR                            # Change to working directory

#module load anaconda3                           # Load module dependencies
#conda init bash
#source ~/.bashrc

conda activate ldm

CUDA_VISIBLE_DEVICES=0,1,2,3 python main.py --base configs/latent-diffusion/midi-vq-4.yaml -r logs/2023-11-29T03-26-41_midi-vq-4/ -t --gpus 0,1,2,3
