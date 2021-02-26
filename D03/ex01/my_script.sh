#!/bin/sh

python3 -m pip --version | cut -d' ' -f1 -f2
#mkdir -p "local_lib"
#cd "local_lib"
GITHUB_URL="https://github.com/jaraco/path.git"
python3 -m pip install --upgrade pip --target=local_lib --force-reinstall git+$GITHUB_URL > install_path.log
python3 my_program.py
