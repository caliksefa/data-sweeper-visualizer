import pandas as pd

def load_data(file_path):
    """Loads CSV data into a Pandas DataFrame"""

    try:
        
        dataframe = pd.read_csv(file_path)
        print(f"Success: Data loaded from {file_path}")
        return dataframe
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

if __name__ == "__main__":
    
    df = load_data("raw_data.csv")

    if df is not None :
        print("\n--- First 5 Rows of Dataset ---")
        print(df.head())


        print("\n--- Dataset Technical Info ---")
        print(df.info())
