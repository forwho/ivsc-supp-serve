import pandas as pd
import shutil
import os
import numpy as np

def data_organize(spath,tpath):
    #spath="/shared/su_group/User/md1weih/CamCAN/cc700/mri/pipeline/release004/BIDS_20190411/"
    #tpath="/mnt/parscratch/users/md1weih/indi-sc/camcan"
    
    demo=pd.read_csv("%s/../demo.csv" % tpath)
    camcan=demo.loc[demo["center"]!=3]
    subids=camcan["id"].to_numpy()
    subids=np.reshape(subids,(50,17))
    for i in range(subids.shape[0]):
        os.makedirs("%s/subset_%02d" % (tpath, i))
        shutil.copy("%s/anat/dataset_description.json" % spath,"%s/subset_%02d" % (tpath, i))
        for j in subids[i]:
            if os.path.exists("%s/anat/%s/anat/%s_T1w.nii.gz" % (spath,j,j)) and os.path.exists("%s/dwi/%s/dwi/%s_dwi.json" %   (spath,j,j)):
                os.makedirs("%s/subset_%02d/%s/anat" % (tpath, i, j))
                os.makedirs("%s/subset_%02d/%s/dwi" % (tpath, i, j))
                shutil.copy("%s/anat/%s/anat/%s_T1w.json" % (spath,j,j), "%s/subset_%02d/%s/anat" % (tpath, i, j))
                shutil.copy("%s/anat/%s/anat/%s_T1w.nii.gz" % (spath,j,j), "%s/subset_%02d/%s/anat" % (tpath, i, j))
    
                shutil.copy("%s/dwi/%s/dwi/%s_dwi.json" % (spath,j,j), "%s/subset_%02d/%s/dwi" % (tpath, i, j))
                shutil.copy("%s/dwi/%s/dwi/%s_dwi.nii.gz" % (spath,j,j), "%s/subset_%02d/%s/dwi" % (tpath, i, j))
                shutil.copy("%s/dwi/%s/dwi/%s_dwi.bval" % (spath,j,j), "%s/subset_%02d/%s/dwi" % (tpath, i, j))
                shutil.copy("%s/dwi/%s/dwi/%s_dwi.bvec" % (spath,j,j), "%s/subset_%02d/%s/dwi" % (tpath, i, j))