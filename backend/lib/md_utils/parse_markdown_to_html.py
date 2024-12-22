from flask import Flask, render_template_string
import markdown
import os

app = Flask(__name__)

def parse_markdown_to_html(file_path: str) -> str:
  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()
    return markdown.markdown(content)
  else:
    return "The file was not found"

def display_markdown(html_content: str) -> str:
    return render_template_string("""
      <div style="border: 1px solid #ccc; padding: 1em;">
        {{ html_content|safe }}
      </div>
    """, html_content=html_content)