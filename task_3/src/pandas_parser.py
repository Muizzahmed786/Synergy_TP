import pandas as pd

def read_csv_pandas(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def calculate_summary_pandas(df: pd.DataFrame) -> dict:
    submitted_df = df[df['submitted'] == 'yes']
    
    total_students = len(df)
    submitted_students = len(submitted_df)
    missing_students = len(df[df['submitted'] == 'no'])
    avg_score = float(submitted_df['score'].mean())
    highest_score = int(submitted_df['score'].max())
    lowest_score = int(submitted_df['score'].min())
    highest_scorer_name = submitted_df[submitted_df['score'] == highest_score]['name'].iloc[0]
    lowest_scorer_name = submitted_df[submitted_df['score'] == lowest_score]['name'].iloc[0]
    domain_avg_score = {domain: float(val) for domain, val in submitted_df.groupby('domain')['score'].mean().items()}
    
    not_submitted = df[df['submitted'] == 'no']['name'].tolist()
    below_5 = df[df['score'] < 5]['name'].tolist()

    summary = {
        "Total students" : total_students,
        "Submitted students" : submitted_students,
        "Missing students" : missing_students,
        "Average score" : avg_score,
        "Domain wise Average score" : domain_avg_score,
        "Highest score" : highest_score,
        "Highest scorer" : highest_scorer_name,
        "Lowest score" : lowest_score,
        "Lowest scorer name" : lowest_scorer_name,
        "Not submitted" : not_submitted,
        "Scores below 5" : below_5
    }

    return summary