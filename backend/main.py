import threading
import time
from lib.flask.core import create_flask_app, set_shared_data
from lib.md_utils.list_markdown_metadata import read_metadata_from_folder

shared_data = {}
lock = threading.Lock()


def flask_thread_function():
  app = create_flask_app()
  set_shared_data(shared_data)
  app.run(debug=True, use_reloader=False)


def data_updater_thread_function(folder_path: str):
  global shared_data
  while True:
    with lock:
      new_data = read_metadata_from_folder(folder_path)
      shared_data.clear()
      shared_data.update(new_data)
    time.sleep(5)


if __name__ == '__main__':
  flask_thread = threading.Thread(target=flask_thread_function)
  flask_thread.start()

  directory_to_scan = "./data/markdown_files"
  file_traverse_thread = threading.Thread(
      target=data_updater_thread_function, args=(
          directory_to_scan,))
  file_traverse_thread.start()

  flask_thread.join()
  file_traverse_thread.join()