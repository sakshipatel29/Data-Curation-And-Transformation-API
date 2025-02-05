# 🚀 TransformX-Data-API

TransformX-Data-API is a data curation API built with Flask and FastAPI to perform various data transformation operations such as renaming columns, filtering data, unit conversions, handling missing values, and removing duplicates.

## 📂 Project Setup

### 1️⃣ Create Project Directory
```sh
mkdir data-curation-api
cd data-curation-api

```

## 🔥 Backend Setup (Flask & FastAPI)

### 1️⃣ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows (Command Prompt)
```
### 2️⃣ Install Dependencies

```sh
pip install flask fastapi uvicorn pandas flask-cors werkzeug xmltodict
```
### 📌 Dependencies Breakdown:
Flask → Web framework for building APIs
FastAPI → High-performance API framework
Pandas → Data transformation and cleaning
Werkzeug → Secure file handling
Flask-CORS → Enable Cross-Origin Resource Sharing
xmltodict → Convert XML data into JSON


### 🛠️ API Features
TransformX-Data-API provides RESTful APIs to perform the following operations on data:

✅ Column Renaming
✅ Filtering Conditions
✅ Unit Conversions
✅ Handling Missing Values
✅ Removing Duplicates


### 🚀 Start the Backend Server
Run the Flask server:
```sh
python app.py
```
Run FastAPI:
```sh
uvicorn app:app --reload
```
### 🔹 Happy Coding! 🚀
