#!/usr/bin/env bash

TSM_INSTALL_DIR='/opt/tivoli'

export LD_LIBRARY_PATH=$TSM_INSTALL_DIR/tsm/client/api/bin64:$LD_LIBRARY_PATH

python libapitsm64.py
