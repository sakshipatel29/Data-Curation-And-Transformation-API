
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Sample tasks list
tasks = []

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Route to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if 'task' not in data:
        return jsonify({"error": "Task field is required"}), 400
    
    task = {"id": len(tasks) + 1, "task": data['task']}
    tasks.append(task)
    return jsonify({"message": "Task added successfully", "task": task}), 201

# Route to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    format = request.form['format']  # CSV, JSON, XML
    # process and validate file, store in memory or cloud
    return {"message": "File uploaded successfully"}

@app.route('/transform', methods=['POST'])
def transform_data():
    transformations = request.json['transformations']
    # Apply transformations using pandas or custom logic
    return {"message": "Data transformed successfully"}

@app.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    # Fetch the file from storage
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
