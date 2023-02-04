#!/bin/bash

# This script is used to clean unnecessary generated files/folders.

remove_eggs() {
  # The directory path is sent as the first argument
  cd $1
  rm -rf build
  rm -rf *.egg-info
  rm -rf dist
  cd ..
}

# remove build files from components
remove_eggs Core

# remove db
cd tim08
rm *.sqlite3
cd ..

cd Core
rm -rf build
rm -rf *.egg-info
rm -rf dist
cd ..
cd file_system_parser
rm -rf build
rm -rf *.egg-info
rm -rf dist
cd ..
cd complex_view_plugin
rm -rf build
rm -rf *.egg-info
rm -rf dist
cd ..
cd simple_view_plugin
rm -rf build
rm -rf *.egg-info
rm -rf dist
cd .. 
cd twitter_api_plugin
rm -rf build
rm -rf *.egg-info
rm -rf dist
cd ..
pip uninstall coree -y
pip uninstall fsp -y
pip uninstall twp -y
pip uninstall svp -y
pip uninstall cvp -y
.
cd Core
python setup.py install
cd ..
cd file_system_parser
python setup.py install
cd .. 
cd twitter_api_plugin
python setup.py install
cd ..
cd simple_view_plugin
python setup.py install
cd ..
cd complex_view_plugin
python setup.py install