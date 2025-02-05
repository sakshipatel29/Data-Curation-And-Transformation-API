import os

# Define file storage paths
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

# Allowed file extensions
ALLOWED_EXTENSIONS = {"csv", "json", "xml"}

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
