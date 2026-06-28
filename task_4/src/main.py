import json
import sys
from clean_data import (
    load_data, generate_summary, remove_duplicates, standardize_domains,
    clean_attendance, clean_scores, clean_study_hours, clean_height,
    clean_weight, clean_submitted, handle_missing_values, handle_invalid_values,
    save_cleaned_data, write_report
)

from validate_data import validate_cleaned_data

def main():
    input_csv_path = sys.argv[1]
    output_csv_path = sys.argv[2]
    
    summary_before_path = "task_4/output/summary_before.json"
    summary_after_path = "task_4/output/summary_after.json"
    report_path = "task_4/output/cleaning_report.md"

    df = load_data(input_csv_path)

    summary_before = generate_summary(df)
    with open(summary_before_path, 'w') as file:
        json.dump(summary_before, file, indent=4)

    df = remove_duplicates(df)
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    
    df = handle_missing_values(df)
    df = handle_invalid_values(df)

    summary_after = generate_summary(df)
    with open(summary_after_path, 'w') as file:
        json.dump(summary_after, file, indent=4)

    validation_passed = validate_cleaned_data(df)
    
    if validation_passed:
        save_cleaned_data(df, output_csv_path)
        write_report(report_path)
    else:
        print("Error in validation test")

if __name__ == "__main__":
    main()