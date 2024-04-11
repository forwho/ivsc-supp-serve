import pandas as pd
import shutil
import os
import numpy as np

def data_organize(spath1,spath2,tpath):
    #spath2="/shared/su_group/User/md1weih/CamCAN/cc700/mri/pipeline/release004/BIDS_20190411/"
    #tpath="/mnt/parscratch/users/md1weih/indi-sc/camcan"
    
    demo=pd.read_csv("%s/../demo.csv" % tpath)
    camcan=demo.loc[demo["center"]!=3]
    subids=camcan["id"].to_numpy()
    subids=np.reshape(subids,(50,17))
    center=camcan["center"].to_numpy()
    center=np.reshape(center,(50,17))
    for i in range(50):
        os.makedirs("%s/subset_%02d" % (tpath, i))
        shutil.copy("%s/anat/dataset_description.json" % spath2,"%s/subset_%02d" % (tpath, i))
        for j in range(17):
            if center[i,j]==1:
                if os.path.exists("%s/%s_V1_MR/unprocessed/Diffusion" % (spath1,subids[i,j])) and os.path.exists("%s/%s_1_MR/unprocessed/T1w_MPR_vNav_4e_e1e2_mean" % (spath1,subids[i,j])):
                    os.makedirs("%s/subset_%02d/sub-%s/anat" % (tpath, i, subids[i,j]))
                    os.makedirs("%s/subset_%02d/sub-%s/dwi" % (tpath, i, subids[i,j]))

                    if os.path.exists("%s/%s_V1_MR/unprocessed/T1w_MPR_vNav_4e_e1e2_mean/%s_V1_MR_T1w_MPR_vNav_4e_e1e2_mean.nii.gz" % (spath1,subids[i,j],subids[i,j])):
                        shutil.copy("%s/%s_V1_MR/unprocessed/T1w_MPR_vNav_4e_e1e2_mean/%s_V1_MR_T1w_MPR_vNav_4e_e1e2_mean.nii.gz" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/anat/sub-%s_T1w.nii.gz" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/T1w_MPR_vNav_4e_e1e2_mean/%s_V1_MR_T1w_MPR_vNav_4e_e1e2_mean.json" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/anat/sub-%s_T1w.json" % (tpath, i, subids[i,j],subids[i,j]))
                        

                    if os.path.exists("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_AP.nii.gz" % (spath1,subids[i,j],subids[i,j])):
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_AP.nii.gz" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-1_dwi.nii.gz" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_AP.json" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-1_dwi.json" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_AP.bval" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-1_dwi.bval" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_AP.bvec" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-1_dwi.bvec" % (tpath, i, subids[i,j],subids[i,j]))

                    if os.path.exists("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_PA.nii.gz" % (spath1,subids[i,j],subids[i,j])):
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_PA.nii.gz" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-1_dwi.nii.gz" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_PA.json" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-1_dwi.json" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_PA.bval" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-1_dwi.bval" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir98_PA.bvec" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-1_dwi.bvec" % (tpath, i, subids[i,j],subids[i,j]))

                    if os.path.exists("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_AP.nii.gz" % (spath1,subids[i,j],subids[i,j])):
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_AP.nii.gz" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-2_dwi.nii.gz" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_AP.json" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-2_dwi.json" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_AP.bval" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-2_dwi.bval" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_AP.bvec" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-AP_run-2_dwi.bvec" % (tpath, i, subids[i,j],subids[i,j]))

                    if os.path.exists("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_PA.nii.gz" % (spath1,subids[i,j],subids[i,j])):
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_PA.nii.gz" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-2_dwi.nii.gz" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_PA.json" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-2_dwi.json" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_PA.bval" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-2_dwi.bval" % (tpath, i, subids[i,j],subids[i,j]))
                        shutil.copy("%s/%s_V1_MR/unprocessed/Diffusion/%s_V1_MR_dMRI_dir99_PA.bvec" % (spath1,subids[i,j],subids[i,j]),"%s/subset_%02d/sub-%s/dwi/sub-%s_dir-PA_run-2_dwi.bvec" % (tpath, i, subids[i,j],subids[i,j]))



            elif center[i,j]==2:
                if os.path.exists("%s/anat/%s/anat/%s_T1w.nii.gz" % (spath2,subids[i,j],subids[i,j])) and os.path.exists("%s/dwi/%s/dwi/%s_dwi.json" %   (spath2,subids[i,j],subids[i,j])):
                    os.makedirs("%s/subset_%02d/%s/anat" % (tpath, i, subids[i,j]))
                    os.makedirs("%s/subset_%02d/%s/dwi" % (tpath, i, subids[i,j]))

                    if os.path.exists("%s/anat/%s/anat/%s_T1w.json" % (spath2,subids[i,j],subids[i,j])):
                        shutil.copy("%s/anat/%s/anat/%s_T1w.json" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/anat" %     (tpath, i, subids[i,j]))
                        shutil.copy("%s/anat/%s/anat/%s_T1w.nii.gz" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/anat" % (tpath, i,  subids[i,j]))

                    if os.path.exists("%s/dwi/%s/dwi/%s_dwi.json" % (spath2,subids[i,j],subids[i,j])):
                        shutil.copy("%s/dwi/%s/dwi/%s_dwi.json" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/dwi" %    (tpath, i, subids[i,j]))
                        shutil.copy("%s/dwi/%s/dwi/%s_dwi.nii.gz" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/dwi" %  (tpath, i, subids[i,j]))
                        shutil.copy("%s/dwi/%s/dwi/%s_dwi.bval" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/dwi" %    (tpath, i, subids[i,j]))
                        shutil.copy("%s/dwi/%s/dwi/%s_dwi.bvec" % (spath2,subids[i,j],subids[i,j]), "%s/subset_%02d/%s/dwi" %    (tpath, i, subids[i,j]))