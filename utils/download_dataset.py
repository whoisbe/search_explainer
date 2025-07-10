# utils/dataset.py

import kagglehub
import shutil
import os

DEFAULT_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
DEFAULT_FILENAME = "moviesData.csv"

def download_tmdb_dataset(data_dir=DEFAULT_DATA_DIR, filename=DEFAULT_FILENAME):
    """
    Downloads the TMDB dataset from KaggleHub and copies the main CSV to the data directory.
    """
    print("🔽 Downloading TMDB dataset from KaggleHub...")
    try:
        path = kagglehub.dataset_download("israrqayyum11/the-movie-database-tmdb")
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        return

    print("📂 Dataset downloaded at:", path)

    os.makedirs(data_dir, exist_ok=True)

    source_file = os.path.join(path, filename)
    dest_file = os.path.join(data_dir, filename)

    if not os.path.exists(source_file):
        print(f"❌ Source file '{source_file}' not found.")
        return

    shutil.copy(source_file, dest_file)
    print(f"✅ Successfully copied '{filename}' to '{data_dir}'")

if __name__ == "__main__":
    download_tmdb_dataset()
