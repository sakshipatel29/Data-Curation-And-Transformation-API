import os
import pandas as pd
import json
import xmltodict

def process_uploaded_file(file_path, output_folder, transformations=None):
    """
    Processes uploaded files with transformations such as:
    - Column renaming
    - Row filtering
    - Unit conversion
    - Removing duplicates
    - Filling missing values
    """
    filename = os.path.basename(file_path)
    file_extension = filename.rsplit(".", 1)[1].lower()
    processed_file_path = os.path.join(output_folder, f"processed_{filename}")

    try:
        # Load file into DataFrame
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

        # 🛠 Data Cleaning
        df.drop_duplicates(inplace=True)  # Remove duplicates
        df.fillna("N/A", inplace=True)  # Replace missing values

        # 🛠 Apply Transformations (if provided)
        if transformations:
            if "rename_columns" in transformations:
                df.rename(columns=transformations["rename_columns"], inplace=True)

            if "filter_rows" in transformations:
                for col, condition in transformations["filter_rows"].items():
                    df = df.query(f"{col} {condition}")  # Example: price > 50

            if "unit_conversion" in transformations:
                for col, conversion in transformations["unit_conversion"].items():
                    if conversion == "in_to_cm":
                        df[col] = df[col].astype(float) * 2.54  # Inches to cm
                    elif conversion == "ft_to_m":
                        df[col] = df[col].astype(float) * 0.3048  # Feet to meters
                    elif conversion == "fahrenheit_to_celsius":
                        df[col] = (df[col].astype(float) - 32) * (5/9)  # F to C

        # Save processed file
        df.to_csv(processed_file_path, index=False)
        return processed_file_path

    except Exception as e:
        return str(e)
