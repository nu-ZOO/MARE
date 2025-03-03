#################################################################################
# SIMPLE H5 TO ROOT CONVERTER
# John Waiton (03/03/25), for Miguel hehe
#################################################################################
# REQUIREMENTS
#################################################################################
# 
#       1. MULE installed in location on LINE XYZ, I can show you how its quick
#       2. MULE conda environment actualised (type `source setup.sh` in MULE/)
#       3. The two extra packages not yet included in MULE:
#           - uproot
#           - awkward_pandas
#       Install them in the terminal with `pip install X` where X is the package
#################################################################################
# USAGE
#################################################################################
#
# In your CLI, type:
#       python3 root_convert.py file_in.h5 file_out.root
#
# It should work automatically.
#
#################################################################################
import sys
from sys import byteorder
import warnings
import numpy as np
import h5py
import tables as tb
import pandas as pd

# you're gonna have to pip install this one, sorry. Will add in the future
#!pip install uproot
#!pip install awkward_pandas
import uproot
import awkward_pandas

# local imports
sys.path.append("/home/e78368jw/Documents/MULE/")
import packs.proc.processing_utils as procutil
import packs.core.io as io
#################################################################################


def h5_to_root(file_in, file_out, verbose = 0):

    # load file information to extract sample numbers
    y = io.load_evt_info(file_in)
    samples = y.samples.unique()[0]
    if verbose != 0:
        print(f'File found with samples per event of {samples}.\nLoading now...')
    x = io.load_rwf_info(file_in, samples)
    
    # convert df to data dictionary
    data_dict = {col: x[col].to_numpy() for col in x.columns}

    # write it
    with uproot.recreate(file_out) as file:
        file["rwf"] = data_dict
    
    # visualising
    print(f"{file_in} read out to {file_out}")
    if verbose != 0:
        print(f"Visualising {file_out}")
        # read it back out
        with uproot.open(file_out) as file:
            tree = file["rwf"]
            df_read = tree.arrays(library="pd")  # Convert back to a DataFrame

        print(df_read.head())

    
# read in args
if __name__ == "__main__":
    if len(sys.argv) == 4:
        h5_to_root(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        h5_to_root(sys.argv[1], sys.argv[2])
