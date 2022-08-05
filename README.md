# dlc_mover_script

Python script that traverses a folder structure using a depth-first search algorithm and copies all \*\_p.psarc files to a selected destination folder.

## Variable breakdown

`root_folder` is the root folder where the DLC you want to copy is located. It can have any number of subfolders and it will still only copy the DLC files, not the folder structure.

`target_folder` is Rocksmith's default DLC folder. Should look like `..\Rocksmith2014\dlc`

In order to make this code work, you should change these two variables to match your local folder structure.

## Running it

User needs to have any version of Python 3 installed.

## For Mac users

This script was built with PC in mind, that's why the file pattern used is `*_p.psarc`. In case of Mac users, going to line 21 and changing `("_p.psarc)` to `("_m.psarc)` should work.
