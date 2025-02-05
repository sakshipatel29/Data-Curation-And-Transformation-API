import os
import pandas as pd
import json
import xmltodict

def process_uploaded_file(file_path, output_folder):
    filename = os.path.basename(file_path)
    file_extension = filename.rsplit(".", 1)[1].lower()
    processed_file_path = os.path.join(output_folder, f"processed_{filename}")

    try:
        if file_extension == "csv":
            df = pd.read_csv(file_path)
        elif file_extension == "json":
            with open(file_path, "r") as file:
                data = json.load(file)
            df = pd.DataFrame(data)
        elif file_extension == "xml":
            with open(file_path, "r") as file:
                data = xmltodict.parse(file.read())
            df = pd.DataFrame(data)
        else:
            return None

        # Data Cleaning
        df.drop_duplicates(inplace=True)  # Remove duplicates
        df.fillna("N/A", inplace=True)  # Replace missing values

        # Save processed file
        df.to_csv(processed_file_path, index=False)
        return processed_file_path

    except Exception as e:
        return str(e)
