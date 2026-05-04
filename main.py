import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        dataframe.columns = ['student_id', 'math_score', 'reading_score', 'writing_score', 'study_hours']
        
        print(f"✅ Success: Data loaded from {file_path}")
        return dataframe
    except FileNotFoundError:
        return None

def clean_data(df): 
    """Cleans the dataset by handling missing values."""
    df = df.copy() # Copy of dataset is taken against possible pandas warnings

    print("\n--- Starting Data Cleaning Process ---")
    print("Missing values before cleaning:\n", df.isnull().sum())

    math_mean = df['math_score'].mean()
    reading_mean = df['reading_score'].mean()
    writing_mean = df['writing_score'].mean()

    df['math_score'] = df['math_score'].fillna(math_mean)
    df['reading_score'] = df['reading_score'].fillna(reading_mean)
    df['writing_score'] = df['writing_score'].fillna(writing_mean)
    
    df = df.dropna(subset=['study_hours'])

    print("\nMissing values after cleaning:\n", df.isnull().sum())
    return df

def visualize_data(df):
    """Generates a scatter plot to analyse study hours vs. math scores."""
    print("\n--- Generating Visualization ---")

    plt.figure(figsize=(10,6))
    plt.scatter(df['study_hours'], df['math_score'], color='blue', alpha=0.7)

    plt.title('Correlation: Study Hours vs. Math Score', fontsize=14, fontweight='bold')
    plt.xlabel('Study Hours (per week)', fontsize=12)
    plt.ylabel('Math Score (0-100)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)

    output_image = "correlation_plot.png"
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show() # Grafiği ekranda göstermek için eklendi

    print(f"Success: Plot generated and saved as {output_image}")


if __name__ == "__main__":
    # Load Data
    raw_df = load_data("raw_data.csv")

    if raw_df is not None:
       cleaned_df = clean_data(raw_df)
       visualize_data(cleaned_df)