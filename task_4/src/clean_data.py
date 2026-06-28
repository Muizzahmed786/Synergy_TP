import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def generate_summary(df: pd.DataFrame) -> pd.DataFrame:
    total_entries = int(len(df))
    duplicate_entries = int(df.duplicated().sum())
    missing_entries = int(df.isnull().sum().sum())
    summary = {
        "Total entries" : total_entries,
        "duplicate_entries" : duplicate_entries,
        "missing entries" : missing_entries 
    }
    return summary

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    return df

def standardize_domains(df: pd.DataFrame) -> pd.DataFrame:
    df['domain'] = df['domain'].str.strip().str.lower()
    domain_hashmap = {
        'ml': 'ML',
        'machine learning': 'ML',
        'web dev': 'Web',
        'web': 'Web',
        'web development': 'Web',
        'electronics': 'Electronics',
        'mechanical': 'Mechanical'
    }
    df['domain'] = df['domain'].replace(domain_hashmap)
    return df

def clean_attendance(df: pd.DataFrame) -> pd.DataFrame:
    df['attendance_percent'] = df['attendance_percent'].astype(str).str.replace('%', '').str.strip()    
    df['attendance_percent'] = pd.to_numeric(df['attendance_percent'], errors='coerce')
    
    return df

def clean_scores(df: pd.DataFrame) -> pd.DataFrame:
    df['score'] = df['score'].astype(str).str.strip().str.lower()    
    scores = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }
    
    df['score'] = df['score'].replace(scores)
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    return df

def clean_study_hours(df: pd.DataFrame) -> pd.DataFrame:
    df['study_hours'] = df['study_hours'].astype(str).str.strip().str.lower()
    hours = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }

    df['study_hours'] = df['study_hours'].replace(hours)
    df['study_hours'] = pd.to_numeric(df['study_hours'], errors='coerce')
    return df

def clean_height(df: pd.DataFrame) -> pd.DataFrame:
    df['height'] = df['height'].astype(str).str.strip().str.lower()

    def convert_cm(height):
        if height == "":
            return None
        if 'cm' in height:
            return float(height.replace('cm', '').strip())
        elif 'm' in height:
            return float(height.replace('m', '').strip()) * 100
        else:
            return float(height)
        
    df['height'] = df['height'].apply(convert_cm)
    df = df.rename(columns={'height': 'height_cm'})
    return df

def clean_weight(df: pd.DataFrame) -> pd.DataFrame:

    df['weight'] = df['weight'].astype(str).str.replace('kg', '', regex=False).str.strip().str.lower()
    df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
    df = df.rename(columns={'weight': 'weight_kg'})
    return df

def clean_submitted(df: pd.DataFrame) -> pd.DataFrame:
    df['submitted'] = df['submitted'].astype(str).str.strip().str.lower()
    status_mapping = {
        'yes': 'yes',
        'y': 'yes',
        'true': 'yes',
        'no': 'no',
        'n': 'no',
        'false': 'no'
    }
    df['submitted'] = df['submitted'].map(status_mapping).fillna('no')
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    if df['attendance_percent'].notna().any():
        median_attendance = df['attendance_percent'].median()
        df['attendance_percent'] = df['attendance_percent'].fillna(median_attendance)
    
    df['score'] = df['score'].fillna(0)
    df['study_hours'] = df['study_hours'].fillna(0)
    df['score'] = df['score'].astype(int)
    df['study_hours'] = df['study_hours'].astype(int)
    
    if df['height_cm'].notna().any():
        mean_height = df['height_cm'].mean()
        df['height_cm'] = df['height_cm'].fillna(mean_height)
        
    if df['weight_kg'].notna().any():
        mean_weight = df['weight_kg'].mean()
        df['weight_kg'] = df['weight_kg'].fillna(mean_weight)

    df['attendance_percent'] = df['attendance_percent'].astype(int)
    df['height_cm'] = df['height_cm'].astype(int)
    df['weight_kg'] = df['weight_kg'].astype(int)
    return df

def handle_invalid_values(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[df['attendance_percent'] < 0, 'attendance_percent'] = 0
    df.loc[df['attendance_percent'] > 100, 'attendance_percent'] = 100
    return df

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved at '{output_path}'.")

def write_report(report_path: str) -> None:
    report = """
    # Task 4: Messy CSV Data Cleaning Report

    ## 1. Removal of duplicate values
    - duplicate entries were detected for student `S005 (Rohan)`.
    - duplicate rows were dropped using the`.drop_duplicates()` filter.

    ## 2. Categorical Value Standardization
    - Inconsistent text naming identified in the `domain` field (`ml`, `ML`, `MACHINE LEARNING`, `Web Dev`, `web`, `web development`).
    - Domain values were made consistent through mapping : `ML`, `Web`, `Electronics`, `Mechanical`.

    ## 3. Unit Normalization
    - Meters were normalized to centimeters, and the header was renamed to `height_cm`.
    - The text unit string `kg` was removed, and converted to float values, and the header was renamed to `weight_kg`.

    ## 5. Out-of-Bounds Boundary Rectification
    - attendance percentage were out of bounds for Dev with `-10` and Naina with `105%`.
    - attendance was capped between `[0, 100]`. Negative values were set to 0 and 100 exceeding values wet set to 100.
    """
    with open(report_path, 'w') as file:
        file.write(report.strip())
    print(f"Report generated '{report_path}'.")