import yaml
import os
from datetime import datetime


def parse_date(date_string: str) -> datetime:
  try:
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
  except ValueError:
    return datetime.strptime(date_string, '%Y-%m-%d')


def read_metadata_from_folder(folder_path) -> dict:
  metadata_dict = {}

  for file_name in os.listdir(folder_path):
    if file_name.endswith('.md'):
      file_path = os.path.join(folder_path, file_name)
      with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

      if lines[0].strip() == '---':
        metadata_end_index = lines[1:].index('---\n') + 1
        metadata_content = ''.join(lines[1:metadata_end_index])
        metadata = yaml.safe_load(metadata_content)

        metadata_dict[file_name] = metadata

  sorted_metadata = sorted(
      metadata_dict.items(),
      key=lambda x: parse_date(
          x[1].get(
              'date',
              '')),
      reverse=True)
  sorted_metadata_dict = dict(sorted_metadata)

  return sorted_metadata_dict
