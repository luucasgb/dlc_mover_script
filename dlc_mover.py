import os
import shutil

# Folder from where DLC should be copied
root_folder = "E:\\Rocksmith DLC"

# Folder where Rocksmith DLC is stored
target_folder = "D:\\Steam\\steamapps\\common\\Rocksmith2014\\dlc"

# Array with a single item, used to keep a count of files moved by script
moved_files = [0]

def traverse_folder_structure(path, count):
	path_content = os.listdir(path)
	if len(path_content) != 0:
		for item in path_content:
			current_item = os.path.join(path, item)
			if not os.path.isfile(current_item):
				traverse_folder_structure(os.path.join(path, current_item), count)
				continue
			if current_item.endswith("_p.psarc"):
				count[0] += 1
				print("Current file: {}".format(item))
				shutil.copy2(current_item, target_folder)

traverse_folder_structure(root_folder, moved_files)
print("{} files were moved.".format(moved_files[0]))
