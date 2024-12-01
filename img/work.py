import os
import shutil

current_directory = os.getcwd()
output_directory = 'G:\\Blog\\themes\\butterfly\\source\\img'

os.makedirs(output_directory, exist_ok=True)
files_to_rename = [f for f in os.listdir(current_directory) if f.startswith('微') and os.path.isfile(f)]
for index, filename in enumerate(files_to_rename, start=1):
    new_name = f"{index}.jpg"
    old_path = os.path.join(current_directory, filename)
    new_path = os.path.join(output_directory, new_name)
    shutil.move(old_path, new_path)

print("文件已成功重命名并移动到指定目录。")
