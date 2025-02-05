from flask import Flask, request, jsonify, send_file, render_template
import os
from werkzeug.utils import secure_filename
from utils.file_handler import process_uploaded_file

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
ALLOWED_EXTENSIONS = {"csv", "json", "xml"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


# Function to check allowed file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to render the UI
@app.route("/")
def home():
    return render_template("index.html")


# Route for uploading a file
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        
        # Process the uploaded file (convert, clean, etc.)
        processed_file_path = process_uploaded_file(file_path, app.config["PROCESSED_FOLDER"])
        
        return render_template("index.html", message="File uploaded successfully!", processed_file=processed_file_path)
    
    return render_template("index.html", error="Invalid file format. Allowed: CSV, JSON, XML")


# Route for downloading processed file
@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    file_path = os.path.join(app.config["PROCESSED_FOLDER"], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
