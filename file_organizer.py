import os
import shutil

source_folder = os.path.expanduser("~/Downloads")  # Adjust the path as necessary
target_folder = os.path.expanduser("~/Sorted")  # Adjust where you'd like the sorted files

# Define file type categories with their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Others": []  # Files with unknown extensions will go here
}


def create_category_folders():
    """Create target directories for each file category."""
    for category in file_categories:
        category_path = os.path.join(target_folder, category)
        os.makedirs(category_path, exist_ok=True)


def move_files():
    """Move files from source to target folder based on their type."""
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    if not os.path.exists(target_folder):
        os.makedirs(target_folder, exist_ok=True)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            # Get the file's extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            # Find the appropriate target folder
            moved = False
            for category, extensions in file_categories.items():
                if extension in extensions:
                    category_path = os.path.join(target_folder, category)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved {filename} to {category_path}")
                    moved = True
                    break

            # Move to "Others" if no matching category found
            if not moved:
                others_path = os.path.join(target_folder, "Others")
                shutil.move(file_path, os.path.join(others_path, filename))
                print(f"Moved {filename} to {others_path}")


if __name__ == "__main__":
    create_category_folders()
    move_files()
