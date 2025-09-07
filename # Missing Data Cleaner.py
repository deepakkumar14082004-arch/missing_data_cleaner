# Missing Data Cleaner
# Author: deepak raj , 2312res240, IIT Patna

import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\nData Loaded Successfully!")
        print(df)
        return df
    except FileNotFoundError:
        print("File not found!")
        exit()

def show_missing_values(df):
    print("\nMissing Values in Each Column:")
    print(df.isnull().sum())

def fill_missing_values(df, method):
    # Fill numeric columns based on selected method
    if method == "1":  # Mean
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
    elif method == "2":  # Median
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].median(), inplace=True)
    elif method == "3":  # Mode
        for col in df.select_dtypes(include=['number']).columns:
            if not df[col].mode().empty:
                df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        print("Invalid choice! Using mean as default.")
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].mean(), inplace=True)

    # Always fill categorical (non-numeric) columns with mode
    for col in df.select_dtypes(exclude=['number']).columns:
        if not df[col].mode().empty:
            df[col].fillna(df[col].mode()[0], inplace=True)

    return df

def save_data(df, original_path):
    new_path = original_path.replace(".csv", "_cleaned.csv")
    df.to_csv(new_path, index=False)
    print(f"\nCleaned file saved as: {new_path}")

if __name__ == "__main__":
    # Sample dataset creation for demonstration
    sample_data = {
        'Name': ['Ravi', 'Meena', 'Kumar'],
        'Age': [28, None, 30],
        'Salary': [None, 45000, 50000]
    }
    sample_df = pd.DataFrame(sample_data)
    sample_file = "sample_dataset.csv"
    sample_df.to_csv(sample_file, index=False)
    print(f"Sample dataset '{sample_file}' created for demo.")

    # Get CSV file path from user
    file_path = input("Enter CSV file name (with .csv): ")
    df = load_data(file_path)

    # Show missing values before cleaning
    show_missing_values(df)

    # Check if there are missing values
    if df.isnull().sum().sum() == 0:
        print("\nNo missing values found. Saving without changes.")
        save_data(df, file_path)
    else:
        print("\nChoose method to fill missing values:")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        choice = input("Enter choice (1-3): ")

        df = fill_missing_values(df, choice)

        print("\nMissing Values After Filling:")
        show_missing_values(df)

        save_data(df, file_path)
