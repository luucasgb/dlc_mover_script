from genericpath import isfile
import os
import shutil

root_folder = "E:\\Torrents\\Rocksmith DLC"
target_folder = "D:\\Lucas\\Downloads\\Teste"
count = [0]

def traverse_folder_structure(path, x):
	path_content = os.listdir(path)
	if len(path_content) != 0:
		for item in path_content:
			current_item = os.path.join(path, item)
			if not os.path.isfile(current_item):
				traverse_folder_structure(os.path.join(path, current_item), x)
				continue
			if current_item.endswith("_p.psarc"):
				x[0] += 1
				shutil.copy2(current_item, target_folder)

traverse_folder_structure(root_folder, count)
print("{} files were moved.}".format(count))