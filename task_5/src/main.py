import sys
from visualize import load_cleaned_data, plot_domain_average_score, plot_attendance_vs_score, plot_submission_status_count

def main():
    input_csv = sys.argv[1]
    output_directory = sys.argv[2]

    df = load_cleaned_data(input_csv)

    plot_domain_average_score(df, output_directory)
    plot_attendance_vs_score(df, output_directory)
    plot_submission_status_count(df, output_directory)
    print(f"Plots saved to : {output_directory}/")

if __name__ == "__main__":
    main()