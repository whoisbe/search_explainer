import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("israrqayyum11/the-movie-database-tmdb")

print("Path to dataset files:", path)

# Copy moviesData.csv to the data directory
print("Copying moviesData.csv to data directory...")
source_file = os.path.join(path, "moviesData.csv")
destination_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

os.makedirs(destination_dir, exist_ok=True)

shutil.copy(source_file, destination_dir)

print(f"Successfully copied 'moviesData.csv' to '{destination_dir}'")