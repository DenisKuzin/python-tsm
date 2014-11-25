#!/usr/bin/env bash

TSM_INSTALL_DIR='/opt/tivoli'

export DSMI_DIR=$TSM_INSTALL_DIR/tsm/client/ba/bin

export DSMI_CONFIG=$DSMI_DIR/dsm.opt

export DSMI_LOG=/var/log/

export LD_LIBRARY_PATH=$TSM_INSTALL_DIR/tsm/client/api/bin64:$LD_LIBRARY_PATH

python libapitsm64.py
