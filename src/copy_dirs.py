import os
import shutil

def copy_dirs(origin, destination):
  shutil.rmtree(destination)
  copy_dirs_internal(origin, destination)

def copy_dirs_internal(origin, destination):
  if not os.path.exists(destination):
    os.mkdir(destination)

  dirs_and_files = os.listdir(origin)

  for entry in dirs_and_files:
    origin_entry = f'{origin}/{entry}'
    destination_entry = f'{destination}/{entry}'

    if os.path.isfile(origin_entry):
      shutil.copy(origin_entry, destination_entry)

    if os.path.isdir(origin_entry):
      os.mkdir(destination_entry)
      copy_dirs_internal(origin_entry, destination_entry)
