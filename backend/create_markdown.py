import os
import random
from datetime import datetime, timedelta
import yaml

template = """---
title: "示例标题 {index}"
date: {date}
tags:
  - python
  - markdown
---

# 正文
这是 Markdown 文档的正文部分。
内容编号：{index}
"""

output_dir = "./data/markdown_files"
os.makedirs(output_dir, exist_ok=True)

file_paths = []

start_date = datetime(2024, 12, 1)

for i in range(20):
  random_hour = random.randint(0, 23)
  random_minute = random.randint(0, 59)

  current_date = start_date + timedelta(days=i)
  date_str = current_date.strftime(
      f"2024-12-{current_date.day:02d} {random_hour:02d}:{random_minute:02d}:00")

  file_content = template.format(
      index=f"{i+1:02}",
      date=f'"{date_str}"')
  file_path = os.path.join(output_dir, f"example_{i+1:02}.md")

  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(file_content)

  file_paths.append(file_path)


def extract_date_from_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    try:
      yaml_content = yaml.safe_load(content.split('---')[1].strip())
      date_str = yaml_content.get('date', None)
      return datetime.strptime(date_str.strip('"'), "%Y-%m-%d %H:%M:%S")
    except Exception as e:
      print(f"Error parsing {file_path}: {e}")
      return None


sorted_file_paths = sorted(file_paths, key=extract_date_from_file)

sorted_file_paths
