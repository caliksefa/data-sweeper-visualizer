# Data Sweeper & Visualizer

An automated data engineering pipeline that ingests raw CSV datasets, handles missing values (NaN) using statistical imputation, and generates correlation visualizations.

## Features

- **Automated Data Cleaning:** Intelligently replaces missing numerical data with column means and drops unrecoverable rows using Pandas.
- **Statistical Visualization:** Generates high-resolution scatter plots to analyze feature correlations (e.g., Study Hours vs. Math Score) using Matplotlib.
- **Strict Isolation:** Built with a clean virtual environment (`venv`) and robust dependency management.

## Tech Stack

- Python 3
- Pandas
- Matplotlib

## How to Run Locally

1. Clone this repository to your local machine.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute the pipeline:
   ```bash
   python main.py
   ```
