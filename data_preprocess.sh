#!/bin/bash
export PATH=$conda_path/envs/pnc/bin/:$PATH
export PYTHONPATH=$conda_path/envs/pnc/lib/python3.8/site-packages/:$PYTHONPATH
data_organize()
{
    source organize_config.sh
    python -c "from data_organize import data_organize;data_organize(\"$spath\",\"$tpath\")"
}
data_organize