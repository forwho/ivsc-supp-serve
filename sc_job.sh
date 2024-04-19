#!/bin/bash

subfolder=""
source organize_config.sh
singularity exec $libpath/qsiprep.simg qsiprep --output-resolution 1.5 --hmc-model eddy --fs-license-file $libpath/freesurfer/license.txt $subfolder $tpath_prep participant
for sub in `ls $tpath_prep/sub-*`
do
  singularity exec $libpath/qsiprep.simg dwi2tensor -fslgrad $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.bvec $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.bval $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.nii.gz $tpath_conn/$sub/dwi/${sub}_space-T1w_desc-preproc_tensor.nii.gz && \
  5ttgen fsl $tpath_prep/$sub/anat/${sub}_desc-preproc_T1w.nii.gz $tpath_prep/$sub/anat/${sub}_desc-preproc_5tt.nii.gz -mask $tpath_prep/$sub/anat/${sub}_desc-brain_mask.nii.gz && \
  5tt2gmwmi $tpath_prep/$sub/anat/${sub}_desc-preproc_5tt.nii.gz $tpath_prep/$sub/anat/${sub}_desc-preproc_gmwmi.nii.gz&&fslsplit $tpath_prep/$sub/anat/${sub}_desc-preproc_5tt.nii.gz $tpath_prep/$sub/anat/${sub}_desc-split_5tt -t && \
  fslmaths $tpath_prep/$sub/anat/${sub}_desc-split_5tt0002.nii.gz -thr 0.95 -bin $tpath_prep/$sub/anat/${sub}_desc-wm_mask.nii.gz && \
  tckgen -algorithm tensor_det -select 0 --seed_grid_per_voxel $tpath_prep/$sub/anat/${sub}_desc-preproc_gmwmi.nii.gz 2 -act $tpath_prep/$sub/anat/${sub}_desc-preproc_5tt.nii.gz -crop_at_gmwmi -fslgrad $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.bvec $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.bval -nthreads 8 -force $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-preproc_dwi.nii.gz $tpath_conn/$sub/dwi/${sub}_space-T1w_desc-preproc_gmwmi.tck && \
  python -c 'from nipype.interfaces import ants;xform=ants.ApplyTransforms(transforms=[\"$tpath_prep/$sub/anat/${sub}_from-MNI152NLin2009cAsym_to-T1w_mode-image_xfm.h5\"],reference_image=\"$tpath_prep/$sub/dwi/${sub}_space-T1w_desc-brain_mask.nii.gz\",input_image=\"/output/BN_Atlas_246_1mm.nii.gz\",output_image=\"$tpath_prep/$sub/dwi/${sub}_space-T1w_desc-atlas_bna.nii.gz\",interpolation=\"MultiLabel\",);xform.run()' && \
  tck2connectome -symmetric -zero_diagonal -force  $tpath_conn/$sub/dwi/${sub}_space-T1w_desc-preproc_gmwmi.tck $tpath_prep/$sub/dwi/${sub}_space-T1w_desc-atlas_bna.nii.gz $tpath_conn/$sub/dwi/${sub}_space-T1w_desc-connectome_bna_gmwmi.csv
done