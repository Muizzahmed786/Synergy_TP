import pandas as pd

def validate_cleaned_data(df: pd.DataFrame) -> bool:
    if df['student_id'].duplicated().any():
        print("Duplicate student id is present.")
        return False
 
    if not df['attendance_percent'].between(0, 100).all():
        print("attendance percentage out of bound (0-100).")
        return False

    domains = {'ML', 'Web', 'Electronics', 'Mechanical'}
    current_domains = set(df['domain'].unique())
    if not current_domains.issubset(domains):
        print(f"Invalid domain values present: {current_domains - domains}")
        return False

    columns = ['student_id', 'name', 'domain', 'attendance_percent', 'score', 'study_hours', 'height_cm', 'weight_kg', 'submitted']
    for col in columns:
        if df[col].isna().any():
            print(f"column '{col}' contains missing values.")
            return False
            
    print("Data cleaning successful.")
    return True