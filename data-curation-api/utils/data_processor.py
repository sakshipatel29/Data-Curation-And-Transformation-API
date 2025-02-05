import pandas as pd
import json
import os

def transform_data(file_path, output_folder, transformations):
    """
    Processes the data file with transformations such as:
    - Column renaming
    - Row filtering
    - Unit conversion
    """
    # Read file based on format
    ext = file_path.split('.')[-1].lower()
    if ext == "csv":
        df = pd.read_csv(file_path)
    elif ext == "json":
        df = pd.read_json(file_path)
    elif ext == "xml":
        df = pd.read_xml(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Apply transformations
    if "rename_columns" in transformations:
        df.rename(columns=transformations["rename_columns"], inplace=True)

    if "filter_rows" in transformations:
        for col, condition in transformations["filter_rows"].items():
            df = df.query(f"{col} {condition}")

    if "unit_conversion" in transformations:
        for col, conversion in transformations["unit_conversion"].items():
            if conversion == "in_to_cm":
                df[col] = df[col] * 2.54  # Inches to cm
            elif conversion == "ft_to_m":
                df[col] = df[col] * 0.3048  # Feet to meters
            elif conversion == "fahrenheit_to_celsius":
                df[col] = (df[col] - 32) * (5/9)  # Fahrenheit to Celsius

    # Save processed file
    processed_filename = "processed_" + os.path.basename(file_path)
    processed_file_path = os.path.join(output_folder, processed_filename)
    
    if ext == "csv":
        df.to_csv(processed_file_path, index=False)
    elif ext == "json":
        df.to_json(processed_file_path, orient="records", indent=4)
    elif ext == "xml":
        df.to_xml(processed_file_path, index=False)
    
    return processed_filename
