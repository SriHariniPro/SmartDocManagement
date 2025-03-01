import os
import shutil
from config import Config

def save_file(file, category):
    """Saves the file into a categorized directory."""
    category_path = os.path.join(Config.UPLOAD_FOLDER, category)
    os.makedirs(category_path, exist_ok=True)
    
    file_path = os.path.join(category_path, file.filename)
    file.save(file_path)
    return file_path

def move_file(file_path, category):
    """Moves an existing file to a new categorized directory."""
    category_path = os.path.join(Config.UPLOAD_FOLDER, category)
    os.makedirs(category_path, exist_ok=True)
    
    new_path = os.path.join(category_path, os.path.basename(file_path))
    shutil.move(file_path, new_path)
    return new_path