from flask import Flask
from flask_cors import CORS
from threading import Lock
from lib.md_utils.parse_markdown_to_html import parse_markdown_to_html
import json

_shared_data = {}
_lock = Lock()
app = Flask(__name__)
CORS(app)

def set_shared_data(data: dict) -> None:
  global _shared_data
  _shared_data = data

def create_flask_app() -> Flask:
  global app

  @app.route('/')
  def home():
    with _lock:
      json_data = json.dumps(_shared_data, indent=4, sort_keys=False)
      return json_data

  @app.route('/md-files/<file_name>')
  def md_files(file_name):
    file_path = f"./data/markdown_files/{file_name}"
    html_content = parse_markdown_to_html(file_path)
    return html_content

  return app